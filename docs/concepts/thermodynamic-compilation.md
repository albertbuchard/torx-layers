# Thermodynamic compilation contract

A logical stochastic kernel and a physical thermodynamic implementation are separate
contracts. TorX Layers must make the relationship explicit.

## Policies

A future strict policy will reject any factor without a native, exact, or certified
target lowering. An approximate policy may admit a variational or otherwise approximate
lowering only within a declared error budget. A hybrid policy may use digital execution,
but every fallback must be visible. Inspection mode may build a model solely to report
capability gaps.

## Lowering categories

- **Native gate lowering** uses an existing TorX stochastic gate directly.
- **Composite circuit lowering** schedules a semantic layer as legal phases of standard
  gates.
- **Directed factor graph lowering** retains a local stochastic factor when circuit
  decomposition is inappropriate.
- **Analytic energy lowering** constructs a known energy-based conditional directly.
- **Variational thermalisation** is reserved for a future public compiler with measured
  per-factor and program-level approximation error.
- **Classical fallback** executes outside the thermodynamic target and is never silent.

## Required report

Reports should eventually state counts of logical pbits, pdits, and pmodes; hidden and
ancilla variables; maximum interaction degree; coupling constraints; circuit phases;
sampling sweeps; embedding overhead; native, exact, approximate, and fallback factors;
calibration needs; and both per-factor and accumulated error estimates.

Compiler estimates must be labelled as estimates. Energy advantage requires executed,
target-specific evidence and cannot be inferred from factor count, API use, or simulator
runtime alone.
