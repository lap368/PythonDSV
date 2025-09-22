"""Tests for Projector component (multi-query approach)."""

from unittest.mock import Mock

import pytest

from src.dsv_core.projector.projector import Projector, ProjectorConfig
from src.dsv_core.store import VirtuosoStore


def test_projector_config_creation() -> None:
    """Test that ProjectorConfig can be created with required values."""
    mock_store = Mock(spec=VirtuosoStore)
    config = ProjectorConfig(store=mock_store, base_uri="http://example.org/test")

    assert config.store == mock_store
    assert config.base_uri == "http://example.org/test"


def test_projector_initialization() -> None:
    """Test that Projector can be initialized with config."""
    mock_store = Mock(spec=VirtuosoStore)
    config = ProjectorConfig(store=mock_store, base_uri="http://example.org/test")

    projector = Projector(config)

    assert projector.config == config
    assert projector.store == mock_store
    assert projector.base_uri == "http://example.org/test"


def test_project_with_basic_shape() -> None:
    """Test project method with a basic shape projection (no sh:node)."""
    mock_store = Mock(spec=VirtuosoStore)

    # Mock query responses for multi-query approach
    mock_store.query.side_effect = [
        # 1. _get_shape_info call
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/age"},
                    },
                ]
            }
        },
        # 2. _get_base_entity_uris call
        {
            "results": {
                "bindings": [
                    {"subject": {"value": "http://example.org/person1"}},
                    {"subject": {"value": "http://example.org/person2"}},
                ]
            }
        },
        # 3. _get_shape_info_simple call (for recursive)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/age"},
                    },
                ]
            }
        },
        # 4. _get_base_properties call
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "name": {"value": "Alice"},
                        "age": {"value": "32"},
                    },
                    {
                        "subject": {"value": "http://example.org/person2"},
                        "name": {"value": "Bob"},
                        "age": {"value": "28"},
                    },
                ]
            }
        },
    ]

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    result = projector.project(
        ["http://test.example.org/rdf-system/.data/people"],
        "http://example.org/PersonShape",
        "http://test.example.org/rdf-system/.projections",
    )

    # Verify structured response
    assert isinstance(result, dict)
    assert "entities" in result
    assert len(result["entities"]) == 2

    # Check entities
    entity1 = result["entities"][0]
    assert entity1["subject"] == "http://example.org/person1"
    assert entity1["name"] == "Alice"
    assert entity1["age"] == "32"

    entity2 = result["entities"][1]
    assert entity2["subject"] == "http://example.org/person2"
    assert entity2["name"] == "Bob"
    assert entity2["age"] == "28"


def test_project_with_sh_node_expansion() -> None:
    """Test project method with sh:node reference expansion."""
    mock_store = Mock(spec=VirtuosoStore)

    # Mock query responses for person with organization
    mock_store.query.side_effect = [
        # 1. _get_shape_info call (PersonWithOrganizationShape)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/worksFor"},
                        "nodeShape": {"value": "http://example.org/OrganizationShape"},
                    },
                ]
            }
        },
        # 1b. _get_shape_info recursive call for OrganizationShape
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/founded"},
                    },
                ]
            }
        },
        # 2. _get_base_entity_uris call (get people)
        {
            "results": {
                "bindings": [
                    {"subject": {"value": "http://example.org/person1"}},
                ]
            }
        },
        # 3. _get_shape_info_simple call (PersonWithOrganizationShape)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/worksFor"},
                        "nodeShape": {"value": "http://example.org/OrganizationShape"},
                    },
                ]
            }
        },
        # 4. _get_base_properties call (get person name)
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "name": {"value": "Alice"},
                    },
                ]
            }
        },
        # 5. _get_relationships call (get worksFor relationships)
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "object": {"value": "http://example.org/org1"},
                    },
                ]
            }
        },
        # 6. _get_shape_info_simple call (OrganizationShape)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/founded"},
                    },
                ]
            }
        },
        # 7. _get_base_properties call (get org properties)
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/org1"},
                        "name": {"value": "TechCorp"},
                        "founded": {"value": "2010-03-15"},
                    },
                ]
            }
        },
    ]

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    result = projector.project(
        [
            "http://test.example.org/rdf-system/.data/people",
            "http://test.example.org/rdf-system/.data/organizations",
        ],
        "http://example.org/PersonWithOrganizationShape",
        "http://test.example.org/rdf-system/.projections",
    )

    # Verify nested structure
    assert isinstance(result, dict)
    assert "entities" in result
    assert len(result["entities"]) == 1

    person = result["entities"][0]
    assert person["subject"] == "http://example.org/person1"
    assert person["name"] == "Alice"

    # Check nested organization
    assert "worksFor" in person
    org = person["worksFor"]
    assert org["subject"] == "http://example.org/org1"
    assert org["name"] == "TechCorp"
    assert org["founded"] == "2010-03-15"


def test_project_with_multiple_values() -> None:
    """Test project method handling multiple values for a property."""
    mock_store = Mock(spec=VirtuosoStore)

    # Mock person working for two organizations
    mock_store.query.side_effect = [
        # 1. _get_shape_info call
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/worksFor"},
                        "nodeShape": {"value": "http://example.org/OrganizationShape"},
                    },
                ]
            }
        },
        # 1b. _get_shape_info recursive call for OrganizationShape
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/name"},
                    },
                ]
            }
        },
        # 2. _get_base_entity_uris call
        {
            "results": {
                "bindings": [
                    {"subject": {"value": "http://example.org/person1"}},
                ]
            }
        },
        # 3. _get_shape_info_simple call
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/worksFor"},
                        "nodeShape": {"value": "http://example.org/OrganizationShape"},
                    },
                ]
            }
        },
        # 4. _get_base_properties call
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "name": {"value": "Alice"},
                    },
                ]
            }
        },
        # 5. _get_relationships call (TWO organizations)
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "object": {"value": "http://example.org/org1"},
                    },
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "object": {"value": "http://example.org/org2"},
                    },
                ]
            }
        },
        # 6. _get_shape_info_simple call (OrganizationShape)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Organization"},
                        "path": {"value": "http://example.org/name"},
                    },
                ]
            }
        },
        # 7. _get_base_properties call (both orgs)
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/org1"},
                        "name": {"value": "TechCorp"},
                    },
                    {
                        "subject": {"value": "http://example.org/org2"},
                        "name": {"value": "StartupCo"},
                    },
                ]
            }
        },
    ]

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    result = projector.project(
        [
            "http://test.example.org/rdf-system/.data/people",
            "http://test.example.org/rdf-system/.data/organizations",
        ],
        "http://example.org/PersonWithOrganizationShape",
        "http://test.example.org/rdf-system/.projections",
    )

    # Verify array handling for multiple values
    person = result["entities"][0]
    assert person["name"] == "Alice"

    # Should be an array of organizations
    assert "worksFor" in person
    orgs = person["worksFor"]
    assert isinstance(orgs, list)
    assert len(orgs) == 2

    # Check both organizations
    org_names = [org["name"] for org in orgs]
    assert "TechCorp" in org_names
    assert "StartupCo" in org_names


def test_project_shape_not_found() -> None:
    """Test project method with non-existent shape."""
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {"results": {"bindings": []}}

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    with pytest.raises(ValueError, match="Shape projection .* not found"):
        projector.project(
            ["http://test.example.org/rdf-system/.data/people"],
            "http://example.org/NonExistentShape",
            "http://test.example.org/rdf-system/.projections",
        )


def test_project_query_failed() -> None:
    """Test project method when SPARQL query fails."""
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = None

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    with pytest.raises(ValueError, match="Shape projection .* not found or query failed"):
        projector.project(
            ["http://test.example.org/rdf-system/.data/people"],
            "http://example.org/PersonShape",
            "http://test.example.org/rdf-system/.projections",
        )


def test_project_no_target_class() -> None:
    """Test project method with shape missing target class."""
    mock_store = Mock(spec=VirtuosoStore)
    mock_store.query.return_value = {
        "results": {
            "bindings": [
                {"path": {"value": "http://example.org/name"}}
                # Missing targetClass
            ]
        }
    }

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    with pytest.raises(ValueError, match="Shape projection .* has no target class"):
        projector.project(
            ["http://test.example.org/rdf-system/.data/people"],
            "http://example.org/InvalidShape",
            "http://test.example.org/rdf-system/.projections",
        )


def test_get_local_name() -> None:
    """Test _get_local_name helper method."""
    mock_store = Mock(spec=VirtuosoStore)
    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    # Test with hash fragment
    assert projector._get_local_name("http://example.org/schema#name") == "name"

    # Test with slash
    assert projector._get_local_name("http://example.org/Person") == "Person"

    # Test without separator
    assert projector._get_local_name("name") == "name"


def test_project_with_empty_graphs() -> None:
    """Test project method with empty graph list."""
    mock_store = Mock(spec=VirtuosoStore)

    # Mock basic shape info
    mock_store.query.side_effect = [
        # Shape info
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/name"},
                    },
                ]
            }
        },
        # Empty entity URIs (no graphs to search)
        {"results": {"bindings": []}},
    ]

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    result = projector.project(
        [],  # Empty graph list
        "http://example.org/PersonShape",
        "http://test.example.org/rdf-system/.projections",
    )

    # Should return empty entities
    assert result == {"entities": []}


def test_project_recursion_prevention() -> None:
    """Test that recursive shape references are handled without infinite loops."""
    mock_store = Mock(spec=VirtuosoStore)

    # Mock circular reference scenario
    mock_store.query.side_effect = [
        # 1. _get_shape_info call (PersonShape references itself)
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/friend"},
                        "nodeShape": {"value": "http://example.org/PersonShape"},  # Self-reference
                    },
                ]
            }
        },
        # 2. _get_base_entity_uris call
        {
            "results": {
                "bindings": [
                    {"subject": {"value": "http://example.org/person1"}},
                ]
            }
        },
        # 3. _get_shape_info_simple call
        {
            "results": {
                "bindings": [
                    {
                        "targetClass": {"value": "http://example.org/Person"},
                        "path": {"value": "http://example.org/friend"},
                        "nodeShape": {"value": "http://example.org/PersonShape"},
                    },
                ]
            }
        },
        # 4. _get_base_properties call (no simple properties)
        {"results": {"bindings": []}},
        # 5. _get_relationships call
        {
            "results": {
                "bindings": [
                    {
                        "subject": {"value": "http://example.org/person1"},
                        "object": {"value": "http://example.org/person2"},
                    },
                ]
            }
        },
        # Recursive call should be prevented, so no more queries
    ]

    config = ProjectorConfig(store=mock_store, base_uri="http://test.example.org/rdf-system")
    projector = Projector(config)

    result = projector.project(
        ["http://test.example.org/rdf-system/.data/people"],
        "http://example.org/PersonShape",
        "http://test.example.org/rdf-system/.projections",
    )

    # Should complete without infinite recursion
    assert isinstance(result, dict)
    assert "entities" in result
