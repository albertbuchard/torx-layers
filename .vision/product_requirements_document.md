# TorX Layers — Product Requirements Document

## Purpose and current release boundary

TorX Layers will provide a Keras-inspired model-building layer over Extropic TorX for typed stochastic and energy-based programs. The current `0.0.0` repository is only a validated architecture scaffold. It must install and build as a Python package, but it must not expose mock layer implementations or imply that a model can already be compiled or sampled.

## Production stack

The package targets Python 3.11 and newer, uses a `src/torx_layers` layout with Hatchling, and uses `uv` to resolve environments and lock dependencies. Extropic TorX is an optional adapter dependency pinned to the compatible 0.0.x line until an explicit compatibility policy is implemented. Ruff, strict Pyright, Pytest and pytest-cov, Python Build, MkDocs Material, pre-commit, Dependabot, and GitHub Actions provide the initial quality and documentation toolchain.

## Functional requirements for future implementation

### Symbolic modelling

The core must represent pbits, finite-cardinality pdits, and continuous pmodes without treating them as ordinary floating-point arrays. Tensor specifications must retain shape, layout, batch semantics, variable role, and eventual wire allocation. Layer and model construction must perform shape and type inference before execution.

### Kernel and layer semantics

Every layer must define a conditional probability kernel or an explicitly documented structural transformation. Energy-native layers must publish the corresponding energy and sampling convention. Shared spatial operations must preserve parameter identity across windows. Pooling must state whether it performs OR, majority, count, sampling, a PCNOT circuit, or another precise stochastic reduction.

### Scheduling and placement

The compiler must enumerate local supports, detect conflicts between overlapping transformations, and produce deterministic schedules in which operations placed in the same TorX circuit phase have legal disjoint support. Scheduling depth and physical placement overhead must be reported.

### Lowering

The architecture must support independent adapters for reference JAX, TorX directed factor graphs, TorX parameterized stochastic circuits, and future Thermalizers compilation. Native, composite, analytic-energy, approximate, and classical-fallback routes must be distinguishable in both machine-readable and human-readable output.

### Thermodynamic policy and reporting

A strict policy must reject unsupported thermodynamic mappings. Approximate policies must require declared error budgets. Hybrid policies may permit classical execution only when the fallback is explicit. Reports must eventually include logical and physical variable counts, hidden and ancilla counts, interaction degree, phases, sampling depth, coupling constraints, embedding estimates, approximation errors, calibration requirements, and fallbacks.

### Scientific evidence

Structural tests must cover shapes, types, windows, padding, strides, dilation, wire allocation, readouts, and stable naming. Scheduling tests must prove non-conflicting phases. Parameter-sharing tests must verify identities and gradient aggregation. Small-system scientific contracts must compare high-level, reference, and lowered distributions with exact state enumeration or statistically justified metrics. Translation-equivariance claims must account for boundaries and sampling uncertainty.

## Initial implementation milestones

The first milestone will establish the symbolic intermediate representation and a JAX reference contract. The second will implement shared one- and two-dimensional stencils, automatic wire allocation, conflict scheduling, and exact TorX circuit lowering. The third will add explicit pooling families and energy-native binary dense and convolutional conditionals. The fourth will add strict compiler policies and thermodynamic reports. Thermalizers integration is deferred until its public API and validation contract are available.

## Repository requirements

The repository must keep the symbolic core independent of TorX imports. Public APIs require type annotations, documentation, and tests. Changes that alter stochastic semantics require mathematical documentation and scientific contract tests. CI must remain bounded and reproducible. No benchmark may claim hardware energy savings without executed target evidence and provenance.

## Non-goals for the scaffold

This bootstrap does not implement layers, download JAX or TorX in its default development environment, publish to PyPI, contact TorX maintainers, run benchmarks, or promise Thermalizers compatibility. It also does not reproduce Keras operations whose deterministic semantics would be misleading on stochastic or thermodynamic targets.

## Acceptance criteria for the scaffold

The package must build and install from the `src` layout without TorX. Ruff, strict Pyright, and Pytest must pass. Documentation and public metadata must describe the architecture and non-implementation status accurately. The code tree must preserve all planned boundaries with module-level contracts. The public repository must contain no credentials, private planning, internal handoffs, personal coordination records, or unsupported scientific claims.
