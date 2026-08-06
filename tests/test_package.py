"""Tests for the installable scaffold boundary."""

from torx_layers import __version__


def test_package_version() -> None:
    """The scaffold exposes only its package version."""
    assert __version__ == "0.0.0"
