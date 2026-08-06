# TorX Layers

TorX Layers is a planned, thermodynamics-aware stochastic layer system for
[Extropic TorX](https://github.com/extropic-ai/torx). The current repository is an
architecture scaffold: it defines the package boundaries, scientific claim policy, and
future acceptance contracts, but it contains no working layers.

The project treats a layer as a conditional stochastic kernel. A friendly model-building
surface must preserve variable types, energy or transition semantics, parameter sharing,
support conflicts, lowering choices, approximation error, and physical constraints.

Start with the [architecture](concepts/architecture.md), then read the [stochastic and
energy semantics](concepts/stochastic-and-energy-semantics.md) and [thermodynamic
compilation contract](concepts/thermodynamic-compilation.md). The [roadmap](roadmap.md)
defines the evidence required before the scaffold becomes an implementation.
