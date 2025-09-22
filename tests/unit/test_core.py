"""Tests for DSV core functionality."""

from src.dsv_core import DSVCore
from src.dsv_core.core import DSVConfig


def test_dsv_core_initialization() -> None:
    """Test that DSVCore can be initialized with explicit local config."""
    # Explicitly set all values to avoid environment variable interference
    config = DSVConfig(store_type="local", base_uri="https://example.com/dsv/")
    dsv = DSVCore(config)

    assert dsv.config.store_type == "local"
    assert dsv.config.base_uri == "https://example.com/dsv/"
    assert dsv.graph is not None
