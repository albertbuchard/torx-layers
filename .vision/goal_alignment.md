# TorX Layers — Goal Alignment

## Executive summary

TorX Layers is intended to make spatial and compositional stochastic programs easier to express without hiding the probability distributions, energy functions, execution constraints, or hardware implications that give those programs meaning. It is an independent, upstream-friendly Python library for researchers and engineers who want a Keras-inspired construction experience over [Extropic TorX](https://github.com/extropic-ai/torx), while retaining explicit thermodynamic semantics. The present repository is an architecture scaffold only. It contains no working layers and makes no claim of hardware compatibility or energy advantage.

The project addresses the gap between TorX's low-level parameterized stochastic circuits and directed factor graphs and a semantic model-building API. A future user should be able to compose typed stochastic tensors, shared spatial kernels, energy-based convolutional conditionals, semantically explicit pooling operations, and sampled readouts. The compiler must then make parameter sharing, wire allocation, legal scheduling, lowering choices, approximation error, and classical fallbacks inspectable.

## Product goal

The product goal is a high-level stochastic layer and model system in which convenience never erases scientific meaning. A layer represents a conditional stochastic kernel, such as a Bernoulli conditional induced by an Ising energy, rather than an ordinary deterministic tensor function. Familiar names are used only when their semantics are precise. For example, binary OR pooling, stochastic majority pooling, and count pooling remain distinct operations instead of being collapsed into an ambiguous `MaxPool2D` label.

The first future proof of value will reproduce TorX's hand-built stochastic convolution example through a reusable shared stencil and explicit pooling layer while preserving its exact gate structure and shared parameters. The next proof will add a genuinely two-dimensional shared stochastic kernel, then an energy-native binary convolution with reference and lowered distributional equivalence evidence.

## Intended users and concepts

The intended users are researchers in probabilistic machine learning, energy-based modelling, stochastic circuits, and thermodynamic computing, plus JAX developers exploring TorX. The central concepts are:

- A **stochastic tensor** is a symbolic collection of pbits, pdits, or pmodes with logical shape, variable type, graph provenance, and clamped, latent, sampled, or readout status.
- A **layer** specifies a conditional stochastic transformation and its parameters. It does not directly imply a physical realization.
- A **program fragment** records factors, parameters, logical and physical wires, schedules, source mappings, and thermodynamic requirements produced by a built layer.
- A **lowering** translates a logical fragment into a TorX directed factor graph, a TorX parameterized stochastic circuit, a reference JAX program, or a future Thermalizers target.
- A **thermodynamic policy** determines whether compilation must be native or certified, may be approximate within a declared error budget, or may use explicit classical fallbacks.
- A **thermodynamic report** explains logical variables, hidden or ancilla variables, interaction degree, execution phases, physical embedding overhead, sampling requirements, approximation error, and fallbacks.

## Public surfaces

The primary future surface is the `torx_layers` Python API. It will support symbolic `Input`, `Layer`, `Model`, and `Sequential` construction; typed tensor specifications; shared stencil and energy-native layer families; explicit stochastic pooling; compiler policies; and human- and machine-readable reports. Documentation will include mathematical semantics, architecture contracts, examples, and evidence-backed benchmarks. There is no web application or service surface in the current product direction.

## Architecture and technical stack

The production package uses Python 3.11 or newer, a `src/torx_layers` package layout, Hatchling as its PEP 517 build backend, and `uv` for dependency resolution and developer environments. TorX 0.0.1 is the initial compatibility reference and is isolated behind optional lowering adapters. Future numerical execution will use JAX in the reference and TorX adapters rather than in the symbolic core.

The repository uses Ruff for formatting and linting, Pyright in strict mode for static analysis, Pytest with coverage for tests, MkDocs Material for documentation, and GitHub Actions for continuous integration across Python 3.11, 3.12, and 3.13. The code architecture separates core symbolic types, kernels, semantic layers, scheduling, lowering adapters, thermodynamic policy/reporting, diagnostics, and scientific testing support.

## Binding constraints

TorX Layers must never infer energy efficiency from API shape alone. Hardware compatibility, physical overhead, mixing behaviour, and energy advantage require evidence from the actual compiler and target. Unsupported or classical paths must never be silent. Ambiguous deterministic neural-network terminology must be rejected or refined into an explicit stochastic operation. The core package must remain independent of unstable TorX internals, with compatibility confined to adapters and contract tests. Public claims must distinguish exact results, sampled estimates, compiler estimates, and unverified design intent.

This scaffold must remain honest: namespace modules document future responsibilities but do not provide fabricated behaviour. Implementation begins only after a design review fixes the intermediate representation and scientific acceptance contracts.
