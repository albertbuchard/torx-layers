# TorX Layers — Product Vision

TorX Layers should let a researcher describe a useful stochastic model at the level of typed inputs, shared local kernels, energy-based conditionals, explicit stochastic reductions, and sampled readouts. The experience should feel approachable to someone familiar with Keras, but the system must never pretend that stochastic circuits are deterministic neural-network layers or that a convenient API guarantees an efficient thermodynamic implementation.

## The modelling experience

A user should be able to define a symbolic input whose elements are pbits, pdits, or pmodes, apply a layer, inspect the inferred output specification, assemble a directed model, and choose a lowering policy. The model summary should connect each friendly layer name to its probability kernel, parameter-sharing pattern, scheduled circuit phases, target capability, approximation status, and physical resource estimate.

Shared stencils will provide the first bridge from hand-built TorX gate loops to reusable spatial programs. Energy-native convolution will represent a shared local conditional distribution whose parameters define an energy, temperature controls stochasticity, and translation equivariance follows from parameter sharing. Pooling will be a family of semantically named reductions rather than a single borrowed deterministic abstraction.

## Architecture

The symbolic core owns variable types, tensor specifications, graph provenance, layers, models, parameters, and intermediate program fragments. Kernel modules define reusable circuit and energy contracts. Layer modules express topology, stencils, convolution, pooling, noise, recurrence, graph operations, and readout. Scheduling modules reason about supports, conflicts, graph colouring, and placement. Lowering adapters isolate TorX and future Thermalizers APIs. Thermodynamic modules define target profiles, policies, capabilities, costs, errors, and reports. Diagnostic and testing modules make compilation and scientific equivalence inspectable.

This separation permits upstream TorX changes without destabilising the public modelling concepts. It also permits a reference implementation to establish mathematical correctness before a physical lowering is available.

## Exact stack

TorX Layers is a typed Python 3.11+ library packaged from `src/torx_layers` with Hatchling and managed with `uv`. The baseline TorX adapter targets `extro-torx` 0.0.1 through an optional dependency. Ruff, strict Pyright, Pytest with coverage, MkDocs Material, pre-commit, GitHub Actions, and Dependabot define the initial engineering system. Apache-2.0 licensing matches TorX and supports future upstream contribution.

## Quality and claim boundary

The project succeeds only if shorter model code remains scientifically transparent. Every compilation path must reveal when it is exact, sampled, approximate, thermalized, or classical. Future benchmarks must measure distributional equivalence, shared-parameter gradients, schedule legality, equivariance, compiler error, and target constraints before making performance or energy claims. The present scaffold is intentionally not a working framework; it is the durable structure in which those claims can later be earned.
