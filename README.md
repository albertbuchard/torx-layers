# TorX Layers

> **Status: architecture scaffold only.** TorX Layers does not yet provide working
> layers, compilation, sampling, or hardware integration. The repository currently
> fixes the public structure and scientific contracts for future implementation.

TorX Layers is an independent, upstream-friendly project for building a Keras-inspired,
thermodynamics-aware layer API over [Extropic TorX](https://github.com/extropic-ai/torx).
Its aim is to make stochastic programs easier to construct without hiding their
conditional distributions, energy functions, shared parameters, legal execution
schedules, lowering choices, approximation errors, or classical fallbacks.

## Why this project exists

TorX 0.0.1 provides parameterized stochastic circuits, directed factor graphs, reusable
factors, and stochastic gates. These are strong execution and composition primitives.
Spatial models still require developers to manage concerns such as windows, wire indices,
parameter maps, readout sites, and overlapping supports at a comparatively low level.

TorX Layers is intended to add a semantic modelling and compiler layer. The project is
not simply shorter syntax for gate-building loops. A future layer will represent a
stochastic conditional kernel and will retain a logical and physical contract.

```text
User-facing stochastic layers
              ↓
Logical stochastic model graph
              ↓
Typed program-fragment intermediate representation
              ↓
Scheduling, placement, and lowering policies
              ↓
TorX DFG / TorX PSC / reference JAX / future Thermalizers
              ↓
Inspectable thermodynamic and approximation report
```

## Intended design direction

The following sketch is **not executable yet**. It illustrates the intended clarity of
the future API:

```python
import torx_layers as txl

inputs = txl.Input(shape=(28, 28, 1), dtype=txl.PBit, name="image")
x = txl.layers.BinaryEnergyConv2D(
    filters=8,
    kernel_size=(3, 3),
    padding="same",
    temperature=1.0,
)(inputs)
x = txl.layers.MajorityPool2D(pool_size=(2, 2), temperature=0.8)(x)
outputs = txl.layers.CategoricalEnergyReadout(classes=10)(x)

model = txl.Model(inputs=inputs, outputs=outputs)
program = model.lower(policy=txl.ThermoPolicy.strict(target="z1"))
program.summary(thermo=True)
```

Names such as `BinaryEnergyConv2D` and `MajorityPool2D` are deliberately explicit. A
binary OR reduction, stochastic majority rule, sampled representative, and pdit count
are different probability kernels and must not be hidden behind one ambiguous pooling
name.

## Repository structure

- `src/torx_layers/core`: symbolic types, tensor specifications, models, parameters, and
  program fragments.
- `src/torx_layers/kernels`: reusable circuit and energy-kernel contracts.
- `src/torx_layers/layers`: future semantic layer families.
- `src/torx_layers/scheduling`: support analysis, conflict detection, colouring, and
  placement.
- `src/torx_layers/lowering`: isolated TorX, reference JAX, and future Thermalizers
  adapters.
- `src/torx_layers/thermo`: target profiles, policies, capabilities, costs, errors, and
  reports.
- `src/torx_layers/diagnostics`: summaries, visualisation, and source maps.
- `src/torx_layers/testing`: future scientific equivalence and gradient helpers.
- `docs`: mathematical, compiler, API, example, and roadmap documentation.
- `tests`: scaffold checks now; structural, integration, and scientific contracts later.

## Development

The core scaffold does not install JAX or TorX. Create a development environment and run
the bounded checks with:

```bash
uv sync --extra dev
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
uv run python -m build
```

Install the optional TorX adapter dependency only when working on lowering:

```bash
uv sync --extra dev --extra torx
```

## Scientific claim policy

Using a high-level API does not make a computation thermodynamic, hardware-compatible,
or energy-efficient. Those properties require an implemented lowering, target-specific
resource and error reports, and executed evidence. Benchmarks must distinguish exact
calculations, sampled estimates, compiler estimates, and hardware measurements.

See the [architecture](docs/concepts/architecture.md), [stochastic and energy
semantics](docs/concepts/stochastic-and-energy-semantics.md), and
[roadmap](docs/roadmap.md) for the planned path.

## License

TorX Layers is licensed under the [Apache License 2.0](LICENSE), matching TorX.
