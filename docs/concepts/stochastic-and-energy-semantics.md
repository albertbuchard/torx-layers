# Stochastic and energy semantics

A conventional neural-network layer often represents a deterministic function
`y = f(x; θ)`. The primary TorX Layers abstraction instead represents a conditional
distribution `y ~ Kθ(· | x)`.

For an energy-native layer with clamped input `x`, sampled output `y`, inverse temperature
`β`, and energy `Eθ(x, y)`, the intended conditional has the form

```text
Kθ(y | x) = exp(-β Eθ(x, y)) / Σy' exp(-β Eθ(x, y')).
```

This equation is a modelling contract, not evidence that a particular target can realise
the distribution without approximation.

## Binary energy convolution

A future binary energy convolution should use a shared local conditional rather than a
sampled deterministic dot product. If inputs and outputs are spins in `{-1, +1}`, a simple
local energy can couple one output spin to a spatial patch with a shared filter and bias.
Reusing the same weights at every location provides translation sharing; temperature
controls stochasticity. Hidden spins may later increase expressiveness but must appear in
resource and error reports.

## Pooling

Pooling names must identify their stochastic operation:

- OR pooling performs a binary OR reduction.
- Majority pooling samples or relaxes toward the sign of a local spin sum under a stated
  energy and temperature.
- Count pooling returns an explicitly cardinal finite variable.
- Sample pooling selects a random representative according to a documented kernel.
- PCNOT pooling reproduces a particular TorX circuit aggregation.
- Energy pooling uses a learnable local conditional energy.

These operations are not interchangeable. A generic `MaxPool2D` alias would be accepted
only if its variable type and exact semantics were unambiguous.

## Structural operations

Reshaping or concatenating stochastic registers may be a zero-cost logical view if it
does not move physical state. Arithmetic combinations are never assumed: combining two
pbits may mean OR, XOR, a categorical count, a probabilistic mixture, or an energy
coupling. The API must require the user to choose.
