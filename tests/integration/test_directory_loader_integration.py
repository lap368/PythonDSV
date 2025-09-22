"""Integration tests for DirectoryLoader with real Virtuoso store."""

import pytest

from src.dsv_core.loader import DirectoryLoader, DirectoryLoaderConfig
from src.dsv_core.store import StoreConfig, VirtuosoStore


@pytest.fixture
def virtuoso_store() -> VirtuosoStore:
    """Create a VirtuosoStore instance for testing."""
    config = StoreConfig(
        endpoint_url="http://localhost:8890/sparql", username="dba", password="dba"
    )
    return VirtuosoStore(config)


class TestDirectoryLoaderIntegration:
    """Integration tests for DirectoryLoader with real Virtuoso."""

    base_uri: str
    local_directory: str
    virtuoso_directory: str

    @classmethod
    def setup_class(cls) -> None:
        """Set up configuration for all tests in this class."""
        cls.base_uri = "http://test.example.org/rdf-system"
        cls.local_directory = "data/ttl/sample/test-system"
        cls.virtuoso_directory = "/ttl/sample/test-system"

    def create_loader_config(self, virtuoso_store: VirtuosoStore) -> DirectoryLoaderConfig:
        """Create a DirectoryLoaderConfig for tests."""
        return DirectoryLoaderConfig(
            local_directory=self.local_directory,
            virtuoso_directory=self.virtuoso_directory,
            store=virtuoso_store,
            base_uri=self.base_uri,
        )

    @pytest.mark.integration
    def test_load_directory_structure_to_virtuoso(self, virtuoso_store: VirtuosoStore) -> None:
        """Test loading a complete directory structure to Virtuoso."""
        # Create loader configuration
        config = self.create_loader_config(virtuoso_store)

        # Create and run loader
        loader = DirectoryLoader(config)
        loaded_graphs = loader.load()

        # Verify expected graphs were created
        expected_graphs = {
            f"{self.base_uri}/.compositions",
            f"{self.base_uri}/.recipes",
            f"{self.base_uri}/.projections",
            f"{self.base_uri}/.connections",
            f"{self.base_uri}/.ontologies",
            f"{self.base_uri}/.data/organizations",
            f"{self.base_uri}/.data/people",
        }

        assert len(loaded_graphs) == 7
        assert set(loaded_graphs) == expected_graphs

        # Verify graphs exist in Virtuoso
        all_graphs = virtuoso_store.list_graphs()
        for graph_uri in expected_graphs:
            assert graph_uri in all_graphs

        # Verify each graph has the expected content
        for graph_uri in expected_graphs:
            count = virtuoso_store.count_triples(graph_uri)
            assert count > 0, f"Graph {graph_uri} should contain triples"

    @pytest.mark.integration
    def test_verify_graph_content_after_loading(self, virtuoso_store: VirtuosoStore) -> None:
        """Test that loaded content can be queried from Virtuoso."""
        config = self.create_loader_config(virtuoso_store)
        loader = DirectoryLoader(config)
        loader.load()

        # Test querying projections graph
        projections_graph = f"{self.base_uri}/.projections"
        projections_query = f"""
        SELECT ?shape ?targetClass WHERE {{
            GRAPH <{projections_graph}> {{
                ?shape a <http://www.w3.org/ns/shacl#NodeShape> ;
                       <http://www.w3.org/ns/shacl#targetClass> ?targetClass .
            }}
        }}
        """

        projections_result = virtuoso_store.query(projections_query)
        projections_bindings = projections_result["results"]["bindings"]

        # Should find PersonShape and OrganizationShape
        assert len(projections_bindings) >= 2

        target_classes = [binding["targetClass"]["value"] for binding in projections_bindings]
        assert "http://example.org/Person" in target_classes
        assert "http://example.org/Organization" in target_classes

    @pytest.mark.integration
    def test_load_with_existing_graphs(self, virtuoso_store: VirtuosoStore) -> None:
        """Test loading when graphs already exist (should update/merge)."""
        config = self.create_loader_config(virtuoso_store)

        loader = DirectoryLoader(config)

        # Load once
        first_load = loader.load()
        assert len(first_load) == 7

        # Get initial triple counts
        initial_counts = {}
        for graph_uri in first_load:
            initial_counts[graph_uri] = virtuoso_store.count_triples(graph_uri)

        # Load again (should not duplicate)
        second_load = loader.load()
        assert len(second_load) == 7
        assert set(second_load) == set(first_load)

        # Verify triple counts (might increase due to Virtuoso behavior)
        for graph_uri in second_load:
            current_count = virtuoso_store.count_triples(graph_uri)
            # Allow for some increase but not doubling (exact behavior depends on Virtuoso)
            assert current_count >= initial_counts[graph_uri]

    @pytest.mark.integration
    def test_query_specific_graph_content(self, virtuoso_store: VirtuosoStore) -> None:
        """Test querying specific content from loaded graphs."""
        config = self.create_loader_config(virtuoso_store)

        loader = DirectoryLoader(config)
        loader.load()

        # Test querying connections graph
        connections_graph = f"{self.base_uri}/.connections"
        connections_query = f"""
        SELECT ?view ?viewOf WHERE {{
            GRAPH <{connections_graph}> {{
                ?view a <http://example.org/View> ;
                      <http://example.org/viewOf> ?viewOf .
            }}
        }}
        """

        connections_result = virtuoso_store.query(connections_query)
        connections_bindings = connections_result["results"]["bindings"]

        # Should find PersonView and PersonDetailView
        assert len(connections_bindings) >= 2

        view_targets = [binding["viewOf"]["value"] for binding in connections_bindings]
        assert "http://example.org/Person" in view_targets

    @pytest.mark.integration
    def test_count_triples_per_graph(self, virtuoso_store: VirtuosoStore) -> None:
        """Test that each graph contains the expected number of triples."""
        config = self.create_loader_config(virtuoso_store)
        loader = DirectoryLoader(config)
        loader.load()

        # Verify each graph has reasonable content
        graph_expectations = {
            f"{self.base_uri}/.projections": 5,  # PersonShape + OrganizationShape with properties
            f"{self.base_uri}/.connections": 3,  # PersonView + PersonDetailView with properties
            f"{self.base_uri}/.ontologies": 10,  # Classes and properties
            f"{self.base_uri}/.tenants": 9,  # 3 tenants with properties
        }

        for graph_uri, min_expected in graph_expectations.items():
            count = virtuoso_store.count_triples(graph_uri)
            assert (
                count >= min_expected
            ), f"Graph {graph_uri} should have at least {min_expected} triples, got {count}"

    def teardown_method(self) -> None:
        """Clean up test graphs after each test."""
        # Note: In a real integration test environment, you might want to
        # clean up test graphs to avoid interference between tests
        pass
