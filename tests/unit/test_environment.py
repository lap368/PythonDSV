"""Tests for environment configuration (without Docker integration)."""

import os
from unittest.mock import patch, MagicMock
from src.dsv_core import DSVCore
from src.dsv_core.core import DSVConfig


class TestEnvironmentConfiguration:
    """Test environment variable configuration."""

    @patch.dict(os.environ, {}, clear=True)
    def test_default_config(self) -> None:
        """Test default configuration values with clean environment."""
        # Clear environment and test true defaults
        config = DSVConfig()

        assert config.store_type == "local"
        assert config.base_uri == "https://example.com/dsv/"
        assert config.virtuoso_endpoint == "http://localhost:8890/sparql"

    @patch.dict(
        os.environ,
        {
            "DSV_STORE_TYPE": "virtuoso",
            "DSV_BASE_URI": "https://test.example.com/",
            "DSV_VIRTUOSO_ENDPOINT": "http://test:8890/sparql",
            "DSV_DEBUG": "true",
        },
    )
    def test_environment_override(self) -> None:
        """Test that environment variables override defaults."""
        config = DSVConfig()

        assert config.store_type == "virtuoso"
        assert config.base_uri == "https://test.example.com/"
        assert config.virtuoso_endpoint == "http://test:8890/sparql"
        assert config.debug is True

    @patch.dict(
        os.environ,
        {
            "DSV_VIRTUOSO_USERNAME": "testuser",
            "DSV_VIRTUOSO_PASSWORD": "testpass",
            "DSV_DEFAULT_GRAPH": "http://test.com/graph",
        },
    )
    def test_virtuoso_credentials_from_env(self) -> None:
        """Test Virtuoso credentials from environment."""
        config = DSVConfig()

        assert config.virtuoso_username == "testuser"
        assert config.virtuoso_password == "testpass"
        assert config.default_graph == "http://test.com/graph"


class TestCoreIntegration:
    """Test core DSV functionality integration."""

    def test_dsv_core_with_virtuoso_config(self) -> None:
        """Test DSVCore initialization with Virtuoso configuration."""
        config = DSVConfig(store_type="virtuoso")

        # Mock VirtuosoStore to avoid actual network calls
        with patch("src.dsv_core.core.VirtuosoStore") as mock_store_class:
            mock_store_instance = MagicMock()
            mock_store_class.return_value = mock_store_instance

            dsv = DSVCore(config)

            # Verify store was created
            mock_store_class.assert_called_once()
            assert dsv.store == mock_store_instance

    def test_local_store_configuration(self) -> None:
        """Test configuration for local store."""
        # Explicitly set local store to avoid environment interference
        config = DSVConfig(store_type="local", log_level="DEBUG")
        dsv = DSVCore(config)

        assert config.store_type == "local"
        assert dsv.store is None  # No Virtuoso store for local mode
