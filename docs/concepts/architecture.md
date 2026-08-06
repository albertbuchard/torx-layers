# Architecture

TorX Layers separates the developer-facing model from its physical realisation. This is
necessary because a stochastic conditional can be meaningful before a particular TorX
circuit or thermodynamic target can implement it efficiently.

## Compilation flow

```text
Layer and Model API
        ↓
Typed symbolic graph
        ↓
ProgramFragment intermediate representation
        ↓
Support analysis, scheduling, and placement
        ↓
Target policy and backend lowering
        ↓
Executable program plus capability, cost, and error report
```

The symbolic graph records logical tensors, stochastic variable types, conditional
kernels, parameters, and data flow. A program fragment adds factors, logical and physical
wires, support information, schedules, source maps, and thermodynamic requirements.

## Package boundaries

`core` owns concepts that must remain stable even when TorX changes. `kernels` defines
local stochastic circuit and energy contracts. `layers` gives those contracts shape and
composition semantics. `scheduling` establishes legal concurrent execution. `lowering`
contains all backend-specific imports and translations. `thermo` records target policies,
capabilities, costs, errors, and reports. `diagnostics` preserves transparency from a
friendly layer back to its generated factors and gates. `testing` will provide reusable
scientific comparison helpers.

The core package must not import TorX. A TorX version change should affect the lowering
adapter and its compatibility tests rather than the meaning of a stochastic layer.

## Source and parameter identity

Repeated spatial windows must refer to named parameter identities rather than manually
assigned integer positions. Lowering may expand those identities into backend-specific
parameter maps, but summaries and gradients must retain their relationship to the
high-level layer. Source maps must similarly connect a layer to generated factors, circuit
phases, gates, wires, and readout locations.

## Scheduling

Sliding windows can overlap. TorX parameterized stochastic circuit phases require legal
support relationships, so a compiler must detect conflicts and schedule overlapping
instances across phases. A simple modular schedule can provide a safe reference;
deterministic graph colouring and hardware-aware placement can later reduce depth. Every
strategy must prove schedule legality and report the resulting depth.
