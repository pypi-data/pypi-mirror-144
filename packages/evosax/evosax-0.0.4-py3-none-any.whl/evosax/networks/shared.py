import jax
import jax.numpy as jnp
from flax import linen as nn
import chex


def default_bias_init(scale=0.05):
    return nn.initializers.uniform(scale)


def identity_out(x: chex.Array, num_output_units: int) -> chex.Array:
    """Simple affine layer."""
    x_out = nn.Dense(
        features=num_output_units,
        bias_init=default_bias_init(),
    )(x)
    return x_out


def tanh_out(x: chex.Array, num_output_units: int):
    """Simple affine layer & tanh rectification."""
    x = nn.Dense(
        features=num_output_units,
        bias_init=default_bias_init(),
    )(x)
    return nn.tanh(x)


def categorical_out(
    rng: chex.PRNGKey, x: chex.Array, num_output_units: int
) -> chex.Array:
    """Simple affine layer & categorical sample from logits."""
    x = nn.Dense(
        features=num_output_units,
        bias_init=default_bias_init(),
    )(x)
    x_out = jax.random.categorical(rng, x)
    return x_out


def gaussian_out(
    rng: chex.PRNGKey, x: chex.Array, num_output_units: int
) -> chex.Array:
    """Simple affine layers for mean and log var + gaussian sample."""
    x_mean = nn.Dense(
        features=num_output_units,
        bias_init=default_bias_init(),
    )(x)
    x_log_var = nn.Dense(
        features=1,
        bias_init=default_bias_init(),
    )(x)
    x_std = jnp.exp(0.5 * x_log_var)
    noise = x_std * jax.random.normal(rng, (num_output_units,))
    return x_mean + noise
