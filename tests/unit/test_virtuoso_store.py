"""Tests for VirtuosoStore interface."""

from src.dsv_core import DSVCore
from src.dsv_core.core import DSVConfig
from src.dsv_core.store import StoreConfig, VirtuosoStore


def test_store_config_creation() -> None:
    """Test that StoreConfig can be created with default values."""
    config = StoreConfig(endpoint_url="http://localhost:8890/sparql")

    assert config.endpoint_url == "http://localhost:8890/sparql"
    assert config.username is None
    assert config.password is None
    assert config.default_graph is None


def test_store_config_with_credentials() -> None:
    """Test StoreConfig with authentication credentials."""
    config = StoreConfig(
        endpoint_url="http://localhost:8890/sparql",
        username="dba",
        password="dba",
        default_graph="http://example.com/graph",
    )

    assert config.endpoint_url == "http://localhost:8890/sparql"
    assert config.username == "dba"
    assert config.password == "dba"
    assert config.default_graph == "http://example.com/graph"


def test_virtuoso_store_initialization() -> None:
    """Test that VirtuosoStore can be initialized."""
    config = StoreConfig(endpoint_url="http://localhost:8890/sparql")
    store = VirtuosoStore(config)

    assert store.config == config
    assert store.sparql is not None


def test_dsv_core_with_virtuoso_config() -> None:
    """Test DSVCore initialization with Virtuoso configuration."""
    config = DSVConfig(
        store_type="virtuoso",
        virtuoso_endpoint="http://localhost:8890/sparql",
        virtuoso_username="dba",
        virtuoso_password="dba",
    )

    dsv = DSVCore(config)

    assert dsv.config.store_type == "virtuoso"
    assert dsv.store is not None
    assert isinstance(dsv.store, VirtuosoStore)


def test_dsv_core_with_local_config() -> None:
    """Test DSVCore initialization with local configuration (no Virtuoso)."""
    config = DSVConfig(store_type="local")
    dsv = DSVCore(config)

    assert dsv.config.store_type == "local"
    assert dsv.store is None  # No store initialized for local mode
