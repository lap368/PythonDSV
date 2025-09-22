"""Integration tests for Projector component with real Virtuoso store."""

import pytest

from src.dsv_core.loader import DirectoryLoader, DirectoryLoaderConfig
from src.dsv_core.projector.projector import Projector, ProjectorConfig
from src.dsv_core.store import StoreConfig, VirtuosoStore


@pytest.fixture
def virtuoso_store() -> VirtuosoStore:
    """Create a VirtuosoStore instance for testing."""
    config = StoreConfig(
        endpoint_url="http://localhost:8890/sparql", username="dba", password="dba"
    )
    return VirtuosoStore(config)


@pytest.fixture
def loaded_test_data(virtuoso_store: VirtuosoStore) -> None:
    """Load test data into Virtuoso before running tests."""
    # Load the test system data including projections
    loader_config = DirectoryLoaderConfig(
        local_directory="data/ttl/sample/test-system",
        virtuoso_directory="/ttl/sample/test-system",
        store=virtuoso_store,
        base_uri="http://test.example.org/rdf-system",
    )

    loader = DirectoryLoader(loader_config)
    loader.load()


class TestProjectorIntegration:
    """Integration tests for Projector with real Virtuoso."""

    base_uri: str

    @classmethod
    def setup_class(cls) -> None:
        """Set up configuration for all tests in this class."""
        cls.base_uri = "http://test.example.org/rdf-system"

    def create_projector_config(self, virtuoso_store: VirtuosoStore) -> ProjectorConfig:
        """Create a ProjectorConfig for tests."""
        return ProjectorConfig(
            store=virtuoso_store,
            base_uri=self.base_uri,
        )

    @pytest.mark.integration
    def test_project_basic_person_shape(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting basic PersonShape with real data."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test the basic person shape projection
        result = projector.project(
            [f"{self.base_uri}/.data/people"],
            "http://example.org/PersonShape",
            f"{self.base_uri}/.projections",
        )

        # Verify the result is structured data
        assert isinstance(result, dict)
        assert "entities" in result

        # Should find person instances
        entities = result["entities"]
        assert len(entities) > 0

        # Each entity should have subject, name, and age
        for entity in entities:
            assert "subject" in entity
            assert entity["subject"].startswith("http://example.org/person")
            # name and age should be present for our test data
            assert "name" in entity
            assert "age" in entity
            assert isinstance(entity["name"], str)
            assert isinstance(entity["age"], str)

    @pytest.mark.integration
    def test_project_person_with_organization_shape(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting PersonWithOrganizationShape with sh:node expansion."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test the person with organization shape projection
        result = projector.project(
            [f"{self.base_uri}/.data/people", f"{self.base_uri}/.data/organizations"],
            "http://example.org/PersonWithOrganizationShape",
            f"{self.base_uri}/.projections",
        )

        # Verify the result is structured data
        assert isinstance(result, dict)
        assert "entities" in result

        entities = result["entities"]
        assert len(entities) > 0

        # Find a person with organization data
        person_with_org = None
        for entity in entities:
            if "worksFor" in entity:
                person_with_org = entity
                break

        assert person_with_org is not None, "Should have at least one person with organization"

        # Verify nested organization structure
        org = person_with_org["worksFor"]
        if isinstance(org, list):
            org = org[0]  # Take first if multiple

        assert "subject" in org
        assert org["subject"].startswith("http://example.org/org")
        assert "name" in org
        assert "founded" in org

    @pytest.mark.integration
    def test_project_organization_shape(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting OrganizationShape with real data."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test the organization shape projection
        result = projector.project(
            [f"{self.base_uri}/.data/organizations"],
            "http://example.org/OrganizationShape",
            f"{self.base_uri}/.projections",
        )

        # Verify the result is structured data
        assert isinstance(result, dict)
        assert "entities" in result

        entities = result["entities"]
        assert len(entities) > 0

        # Each organization should have expected properties
        for entity in entities:
            assert "subject" in entity
            assert entity["subject"].startswith("http://example.org/org")
            assert "name" in entity
            assert "founded" in entity

    @pytest.mark.integration
    def test_project_nonexistent_shape(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting a non-existent shape raises appropriate error."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test with a shape that doesn't exist
        with pytest.raises(ValueError, match="not found"):
            projector.project(
                [f"{self.base_uri}/.data/people"],
                "http://example.org/NonExistentShape",
                f"{self.base_uri}/.projections",
            )

    @pytest.mark.integration
    def test_project_with_empty_graph_list(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting with an empty list of graphs."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test with empty graph list
        result = projector.project(
            [], "http://example.org/PersonShape", f"{self.base_uri}/.projections"
        )

        # Should return empty entities since no graphs to search
        assert isinstance(result, dict)
        assert "entities" in result
        assert result["entities"] == []

    @pytest.mark.integration
    def test_generated_query_execution_results(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test that projector returns expected data structure."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Execute projection (now returns structured data directly)
        result = projector.project(
            [f"{self.base_uri}/.data/people"],
            "http://example.org/PersonShape",
            f"{self.base_uri}/.projections",
        )

        # Verify structured data format
        assert isinstance(result, dict)
        assert "entities" in result
        entities = result["entities"]

        assert len(entities) > 0
        for entity in entities:
            # Each entity should have a subject (person URI)
            assert "subject" in entity
            assert "http://example.org/person" in entity["subject"]

    @pytest.mark.integration
    def test_project_with_wrong_projection_graph(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projecting with wrong projection graph URI."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Test with wrong projection graph
        with pytest.raises(ValueError, match="not found"):
            projector.project(
                [f"{self.base_uri}/.data/people"],
                "http://example.org/PersonShape",
                f"{self.base_uri}/.wrong-projections",  # Wrong graph
            )

    @pytest.mark.integration
    def test_project_query_optimization(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test that projector executes efficiently and returns optimized results."""
        config = self.create_projector_config(virtuoso_store)
        projector = Projector(config)

        # Execute projection
        result = projector.project(
            [f"{self.base_uri}/.data/people"],
            "http://example.org/PersonShape",
            f"{self.base_uri}/.projections",
        )

        # Verify result is optimized (no duplicate data, clean structure)
        assert isinstance(result, dict)
        assert "entities" in result
        entities = result["entities"]

        # Should have entities without duplication
        subjects = [entity["subject"] for entity in entities]
        assert len(subjects) == len(set(subjects)), "No duplicate subjects should exist"

        # Each entity should have clean, complete data
        for entity in entities:
            assert "subject" in entity
            # Should have properties without null/empty values for test data
            if "name" in entity:
                assert entity["name"]  # Should not be empty
            if "age" in entity:
                assert entity["age"]  # Should not be empty

    def test_project_with_multiple_values_integration(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test projector handling of multiple values for the same property with real data."""
        projector_config = self.create_projector_config(virtuoso_store)
        projector = Projector(projector_config)

        result = projector.project(
            [
                "http://test.example.org/rdf-system/.data/people",
                "http://test.example.org/rdf-system/.data/organizations",
            ],
            "http://example.org/PersonWithOrganizationShape",
            "http://test.example.org/rdf-system/.projections",
        )

        # Should return structured data
        assert isinstance(result, dict)
        assert "entities" in result

        # Find Eve Martinez who works for multiple organizations
        eve = None
        for entity in result["entities"]:
            if entity.get("name") == "Eve Martinez":
                eve = entity
                break

        assert eve is not None, "Eve Martinez should be found in results"

        # Eve should have multiple organizations in worksFor property
        assert "worksFor" in eve
        works_for = eve["worksFor"]

        # Should be a list (array) since there are multiple values
        assert isinstance(works_for, list), f"worksFor should be a list, got {type(works_for)}"
        assert len(works_for) == 2, f"Eve should work for 2 organizations, got {len(works_for)}"

        # Both organizations should have proper structure
        org_names = []
        for org in works_for:
            assert isinstance(org, dict), f"Each organization should be a dict, got {type(org)}"
            assert "subject" in org
            assert "name" in org
            org_names.append(org["name"])

        # Should include both TechCorp Solutions and DataFlow Systems (based on our test data)
        expected_orgs = {"TechCorp Solutions", "DataFlow Systems"}
        actual_orgs = set(org_names)
        assert expected_orgs == actual_orgs, f"Expected {expected_orgs}, got {actual_orgs}"

    def teardown_method(self) -> None:
        """Clean up test graphs after each test."""
        # Create store instance for cleanup
        config = StoreConfig(
            endpoint_url="http://localhost:8890/sparql", username="dba", password="dba"
        )
        store = VirtuosoStore(config)

        # Clean up all test graphs to prevent interference between tests
        test_graphs = [
            "http://test.example.org/rdf-system/.projections",
            "http://test.example.org/rdf-system/.recipes",
            "http://test.example.org/rdf-system/.compositions",
            "http://test.example.org/rdf-system/.connections",
            "http://test.example.org/rdf-system/.data/organizations",
            "http://test.example.org/rdf-system/.data/people",
            "http://test.example.org/rdf-system/.ontologies",
        ]

        for graph_uri in test_graphs:
            try:
                store.sparql.setQuery(f"CLEAR GRAPH <{graph_uri}>")
                store.sparql.setMethod("POST")
                store.sparql.query()
            except Exception:
                # Ignore errors if graph doesn't exist or can't be cleared
                pass

            except Exception:
                pass
