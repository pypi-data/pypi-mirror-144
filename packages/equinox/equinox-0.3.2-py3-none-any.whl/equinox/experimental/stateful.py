import weakref
from typing import Tuple

import jax
import jax.experimental.host_callback as hcb
import jax.interpreters.batching as batching
import jax.interpreters.xla as xla
import jax.lax as lax

from ..custom_types import Array, PyTree
from ..filters import is_array
from ..module import Module, static_field
from ..tree import tree_at


# So the use of a weak dictionary is a bit of wishful thinking here, really.
# In practice JAX will cache the _IndexObj when it is passed across the hcb.call
# boundary.
# Which at least in part is what we want! We want the cached state to persist for
# as long as the XLA graph it's part of.
# The annoying bit is that even once that XLA graph vanishes, JAX still seems to keep
# things cached somewhere.
_state_cache = weakref.WeakKeyDictionary()


class _IndexObj:
    __slots__ = ("__weakref__",)


class StateIndex(Module):
    """An index for setting or getting a piece of state with
    [`equinox.experimental.get_state`][] or [`equinox.experimental.set_state`][].

    You should typically treat this like a model parameter.

    !!! example

        ```python
        import equinox as eqx
        import equinox.experimental as eqxe
        import jax.numpy as jnp

        class CacheInput(eqx.Module):
            index: eqxe.StateIndex

            def __init__(self, input_shape):
                self.index = eqxe.StateIndex()
                eqxe.set_state(self.index, jnp.zeros(input_shape))

            def __call__(self, x):
                last_x = eqxe.get_state(self.index, x)
                eqxe.set_state(self.index, x)
                print(f"last_x={last_x}, x={x}")

        x = jnp.array([1., 2.])
        y = jnp.array([3., 4.])
        shape = x.shape
        ci = CacheInput(shape)
        ci(x)
        ci(y)
        ```
    """

    obj: _IndexObj = static_field()
    inference: bool

    def __init__(self, inference: bool = False):
        """**Arguments:**

        - `inference`: If `True`, then `equinox.experimental.set_state(index, value)`
            will be disabled, and throw a `RuntimeError`. This is based on the fact
            that we typically don't want to update state (batch norm statistics,
            spectral norm power iterations, etc.) during model inference.
            If you have some other use case for saving state then this can be left at
            `False`.
        """
        self.obj = _IndexObj()
        self.inference = inference

    def unsafe_get(self):
        return _state_cache[self.obj]


# Monkey-patch the batching rule for host_callback.call to work with get_state and set_state.
_have_monkey_patched = False


def _monkey_patch():
    global _have_monkey_patched
    if not _have_monkey_patched:
        _have_monkey_patched = True

        _old_outside_call_impl = hcb.outside_call_p.impl
        _old_outside_call_translation_rule = xla._translations[hcb.outside_call_p]
        _old_outside_call_batching_rule = batching.primitive_batchers[
            hcb.outside_call_p
        ]

        def _outside_call_impl(*arg_flat, arg_treedef, **params):
            leaves = [None] * arg_treedef.num_leaves
            call_type = type(jax.tree_unflatten(arg_treedef, leaves))
            # Not using isinstance for speed. (Questionable choice?)
            if call_type is _GetStateArg:
                arg = jax.tree_unflatten(arg_treedef, arg_flat)
                token_like = jax.tree_map(lambda _: jax.core.token, arg.like)
                arg = tree_at(
                    lambda a: jax.tree_leaves(a.like), arg, jax.tree_leaves(token_like)
                )
                arg_flat = jax.tree_leaves(arg)
            return _old_outside_call_impl(*arg_flat, arg_treedef=arg_treedef, **params)

        def _outside_call_translation_rule(ctx, avals_in, *args, arg_treedef, **kwargs):
            leaves = [None] * arg_treedef.num_leaves
            call_type = type(jax.tree_unflatten(arg_treedef, leaves))
            if call_type is _GetStateArg:
                arg_flat = avals_in[:-2]
                extra_tokens = avals_in[-2:]
                arg = jax.tree_unflatten(arg_treedef, arg_flat)
                token_like = jax.tree_map(lambda _: jax.core.abstract_token, arg.like)
                arg = tree_at(
                    lambda a: jax.tree_leaves(a.like), arg, jax.tree_leaves(token_like)
                )
                arg_flat = jax.tree_leaves(arg)
                avals_in = arg_flat + extra_tokens
            return _old_outside_call_translation_rule(
                ctx, avals_in, *args, arg_treedef=arg_treedef, **kwargs
            )

        def _outside_call_batching_rule(
            arg_flat, batch_axes, *, arg_treedef, result_treedef, **params
        ):
            leaves = [None] * arg_treedef.num_leaves
            call_type = type(jax.tree_unflatten(arg_treedef, leaves))
            if call_type is _GetStateArg:
                arg = jax.tree_unflatten(arg_treedef, arg_flat)
                state = _get_state(arg.index, arg.like, arg.batch_axes + batch_axes)
                state_leaves, state_treedef = jax.tree_flatten(state)
                assert state_treedef == result_treedef
                assert all(
                    a is b for a, b in zip(arg_flat[1:], jax.tree_leaves(arg.like))
                )
                return state_leaves, batch_axes[1:]
            elif call_type is _SetStateArg:
                arg = jax.tree_unflatten(arg_treedef, arg_flat)
                _set_state(arg.index, arg.state, arg.batch_axes + batch_axes)
                return (), ()
            else:
                return _old_outside_call_batching_rule(
                    arg_flat,
                    batch_axes,
                    arg_treedef=arg_treedef,
                    result_treedef=result_treedef,
                    **params
                )

        hcb.outside_call_p.def_impl(_outside_call_impl)
        batching.primitive_batchers[hcb.outside_call_p] = _outside_call_batching_rule
        xla.register_translation(hcb.outside_call_p, _outside_call_translation_rule)


class _GetStateArg(Module):
    index: StateIndex
    like: PyTree[Array]
    batch_axes: Tuple[int] = static_field()


def _get_state_hcb(arg: _GetStateArg) -> PyTree:
    index = arg.index
    batch_axes = arg.batch_axes
    try:
        current_state, current_batch_axes = _state_cache[index.obj]
    except KeyError as e:
        raise KeyError("Cannot get state before it has been set") from e
    if current_batch_axes != batch_axes:
        raise TypeError("`like` and the saved state have different batch axes")
    return current_state


def _get_state(
    index: StateIndex, like: PyTree[Array], batch_axes: Tuple[int]
) -> PyTree:
    if any(not is_array(x) for x in jax.tree_leaves(like)):
        raise TypeError("`like` must be a PyTree containing only JAX arrays")
    _monkey_patch()
    arg = _GetStateArg(index, like, batch_axes)
    like_shape = jax.eval_shape(lambda: like)
    # Will raise an error if `like_shape` does not match the result.
    return hcb.call(_get_state_hcb, arg, result_shape=like_shape)


def get_state(index: StateIndex, like: PyTree[Array]) -> PyTree[Array]:
    """Get some previously saved state.

    **Arguments:**

    - `index`: The index of the state to look up. Should be an instance of
        [`equinox.experimental.StateIndex`][].
    - `like`: A PyTree of JAX arrays of the same shape, dtype, PyTree structure, and
        batch axes as the state being looked up.

    **Returns:**

    Whatever the previously saved state is.

    **Raises:**

    A `TypeError` at trace time if `like` is not a PyTree of JAX arrays.

    A `TypeError` at run time if `like` is not of the same shape, dtype, PyTree
    structure, and batch axes as the retrieved value.

    A `KeyError` at run time if no state has previously been saved with this `index`.

    !!! warning

        This means that your operation will no longer be a pure function.
    """
    return _get_state(index, like, ())


class _SetStateArg(Module):
    index: StateIndex
    state: PyTree[Array]
    batch_axes: Tuple[int] = static_field()


def _set_state_hcb(arg: _SetStateArg) -> None:
    # Note that these checks cannot happen inside `set_state` as we have to consider
    # the possibility in which `set_state` is traced into a jaxpr and then transformed
    # (e.g. vmap'd.)
    # In principle it should be possible to perform these checks at compile time but it
    # would likely require us to create our own primitive? Which in turn wouldn't play
    # well with all the custom primitive handling that experimental.host_callback does?
    index = arg.index
    state = arg.state
    batch_axes = arg.batch_axes
    try:
        current_state, current_batch_axes = _state_cache[index.obj]
    except KeyError:
        pass
    else:
        current_state_shape = jax.eval_shape(lambda: current_state)
        state_shape = jax.eval_shape(lambda: state)
        if current_state_shape != state_shape:
            raise TypeError(
                "New state and old state have different shape, dtype, or PyTree structure"
            )
        if current_batch_axes != batch_axes:
            raise TypeError("New state and old state have different batch axes")
    _state_cache[index.obj] = (state, batch_axes)


def set_state(index: StateIndex, state: PyTree[Array]) -> None:
    """Save a PyTree of JAX arrays as a side-effect.

    **Arguments:**

    - `index`: A key under which to save the state. Should be an instance of
        [`equinox.experimental.StateIndex`][].
    - `state`: An PyTree of JAX arrays to save.

    **Returns:**

    `None`.

    **Raises:**

    A `RuntimeError` at trace time if `index.inference` is truthy.

    A `TypeError` at trace time if `state` is not a PyTree of JAX arrays.

    A `TypeError` at run time if this `index` has previously been used to save a
    `state` with a different shape, dtype, PyTree structure, or batch axes.

    !!! info

        The same `index` can be used multiple times, to overwrite a previously saved
        value. The new and old `state` must both have the same PyTree structure, however.

    !!! warning

        Note that gradient information in `state` will not preserved.

    !!! warning

        This means that your operation will no longer be a pure function. Moreover note
        that the saving-as-a-side-effect may occur even when `set_state` is wrapped in
        `lax.cond` etc. (As e.g. under `vmap` then `lax.cond` is transformed into
        `lax.select`.)
    """
    if index.inference:
        raise RuntimeError("Cannot use `set_state` during inference.")
    return _set_state(index, state, ())


def _set_state(index: StateIndex, state: PyTree[Array], batch_axes: Tuple[int]) -> None:
    if any(not is_array(x) for x in jax.tree_leaves(state)):
        raise TypeError("`state` must be a PyTree containing only JAX arrays")
    _monkey_patch()
    state = jax.tree_map(lax.stop_gradient, state)
    arg = _SetStateArg(index, state, batch_axes)
    hcb.call(_set_state_hcb, arg)
