# Contributing to TorX Layers

TorX Layers is currently in its design phase. Contributions should strengthen the
scientific and compiler contracts before expanding the layer catalogue.

## Before proposing an implementation

Open an issue that states the conditional stochastic kernel, input and output variable
types, parameter-sharing rule, exact or approximate lowering route, scheduling and
physical-support implications, and the evidence that will establish correctness. A
familiar deterministic layer name is not a sufficient specification.

## Development checks

Use Python 3.11 or newer and `uv`:

```bash
uv sync --extra dev
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
uv run python -m build
```

Changes to stochastic semantics must include mathematical documentation and scientific
contract tests. Changes to TorX adapters must include compatibility tests against the
supported TorX version. Do not add performance, thermodynamic, or energy-efficiency
claims without reproducible evidence and clear provenance.

Use `main` for repository work unless the maintainer explicitly approves another branch
for a specific contribution workflow.
