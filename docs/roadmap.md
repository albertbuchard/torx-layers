# Roadmap

## Phase 0: design contracts

Fix the typed stochastic tensor model, layer lifecycle, parameter graph, program-fragment
intermediate representation, lowering capability vocabulary, and error policy. Compare the
design with TorX maintainers' direction before freezing public names.

Exit when the intermediate representation can express the existing TorX stochastic
convolution without ambiguity and every public concept has a precise mathematical role.

## Phase 1: symbolic core and reference backend

Implement types, specifications, symbolic tensors, layers, models, parameters, fragments,
serialisation, and a JAX reference backend.

Exit when models can be constructed and shape-checked and small reference kernels can be
sampled deterministically under controlled seeds.

## Phase 2: shared spatial compiler

Implement circuit kernels, shared one- and two-dimensional stencils, window enumeration,
padding, stride, dilation, wire allocation, support conflicts, deterministic scheduling,
readout allocation, and TorX circuit lowering.

Exit when the existing TorX example is reproduced with the same gates, shared parameters,
readouts, distributions, and gradients through substantially shorter construction code.

## Phase 3: pooling and energy-native layers

Implement PCNOT, OR, majority, count, and sample pooling; binary energy dense and
convolution layers; categorical readout; and reference-versus-lowered scientific tests.

Exit when a small image model has explicit stochastic semantics and passes exact or
statistically justified distributional acceptance criteria.

## Phase 4: thermodynamic policies and reports

Implement target profiles, strict and approximate policies, capability classification,
resource estimates, error accounting, and machine-readable reports.

Exit when no model can silently present a classical or unsupported component as a
thermodynamic implementation.

## Phase 5: future compiler integration

Integrate Thermalizers or another public target compiler only after its API, calibration
requirements, and error guarantees can be tested. Hardware energy claims remain deferred
until reproducible target measurements exist.
