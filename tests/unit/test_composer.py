"""Tests for Composer component."""

from unittest.mock import Mock

import pytest

from src.dsv_core.composer.composer import Composer, ComposerConfig
from src.dsv_core.store import VirtuosoStore


def test_composer_config_creation() -> None:
    """Test that ComposerConfig can be created with required values."""
    mock_store = Mock(spec=VirtuosoStore)
    config = ComposerConfig(store=mock_store, base_uri="http://example.org/test")

    assert config.store == mock_store
    assert config.base_uri == "http://example.org/test"


def test_composer_initialization() -> None:
    """Test that Composer can be initialized with config."""
    mock_store = Mock(spec=VirtuosoStore)
    config = ComposerConfig(store=mock_store, base_uri="http://example.org/test")

    composer = Composer(config)

    assert composer.config == config
    assert composer.store == mock_store
    assert composer.base_uri == "http://example.org/test"


def test_compose_with_single_graph() -> None:
    """Test compose method with a composition containing a single graph."""
    # Mock store and query result
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "results": {
            "bindings": [{"graph": {"value": "http://test.example.org/rdf-system/.data/people"}}]
        }
    }

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test the compose method
    result = composer.compose(
        "dsv:BasicPersonDataComposition", "http://test.example.org/rdf-system/.compositions"
    )

    # Verify the result
    assert result == ["http://test.example.org/rdf-system/.data/people"]

    # Verify the SPARQL query was called correctly
    mock_store.query.assert_called_once()
    called_query = mock_store.query.call_args[0][0]
    assert "dsv:BasicPersonDataComposition" in called_query
    assert "dsv:includesGraphs" in called_query
    assert "rdf:rest*" in called_query
    assert "rdf:first" in called_query
    assert "GRAPH <http://test.example.org/rdf-system/.compositions>" in called_query


def test_compose_with_multiple_graphs() -> None:
    """Test compose method with a composition containing multiple graphs."""
    # Mock store and query result with multiple graphs
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "results": {
            "bindings": [
                {"graph": {"value": "http://test.example.org/rdf-system/.data/people"}},
                {"graph": {"value": "http://test.example.org/rdf-system/.data/organizations"}},
            ]
        }
    }

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test the compose method
    result = composer.compose(
        "dsv:PersonOrgDataComposition", "http://test.example.org/rdf-system/.compositions"
    )

    # Verify the result contains both graphs
    expected_graphs = [
        "http://test.example.org/rdf-system/.data/people",
        "http://test.example.org/rdf-system/.data/organizations",
    ]
    assert result == expected_graphs

    # Verify the query was called
    mock_store.query.assert_called_once()


def test_compose_composition_not_found() -> None:
    """Test compose method when composition is not found."""
    # Mock store returning no results
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {"results": {"bindings": []}}

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test that ValueError is raised
    with pytest.raises(ValueError, match="contains no graphs"):
        composer.compose(
            "dsv:NonExistentComposition", "http://test.example.org/rdf-system/.compositions"
        )


def test_compose_query_failed() -> None:
    """Test compose method when SPARQL query fails."""
    # Mock store returning None (query failure)
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = None

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test that ValueError is raised
    with pytest.raises(ValueError, match="not found or query failed"):
        composer.compose("dsv:SomeComposition", "http://test.example.org/rdf-system/.compositions")


def test_compose_malformed_query_result() -> None:
    """Test compose method with malformed query result."""
    # Mock store returning malformed result
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "results": {
            "bindings": [
                {
                    # Missing "graph" key or malformed structure
                    "other_field": {"value": "some_value"}
                }
            ]
        }
    }

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test that ValueError is raised
    with pytest.raises(ValueError, match="malformed graph list"):
        composer.compose(
            "dsv:MalformedComposition", "http://test.example.org/rdf-system/.compositions"
        )


def test_compose_missing_results_structure() -> None:
    """Test compose method with missing results structure."""
    # Mock store returning result without proper structure
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "some_other_field": "value"
        # Missing "results" key
    }

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test that ValueError is raised
    with pytest.raises(ValueError, match="not found or query failed"):
        composer.compose(
            "dsv:BadStructureComposition", "http://test.example.org/rdf-system/.compositions"
        )


def test_compose_empty_graph_values() -> None:
    """Test compose method when bindings exist but have no valid graph values."""
    # Mock store returning bindings without valid graph values
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "results": {
            "bindings": [
                {
                    "graph": {
                        # Missing "value" key
                        "type": "uri"
                    }
                }
            ]
        }
    }

    config = ComposerConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    composer = Composer(config)

    # Test that ValueError is raised
    with pytest.raises(ValueError, match="malformed graph list"):
        composer.compose(
            "dsv:EmptyValuesComposition", "http://test.example.org/rdf-system/.compositions"
        )
