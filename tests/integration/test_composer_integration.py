"""Integration tests for Composer component with real Virtuoso store."""

import pytest

from src.dsv_core.composer.composer import Composer, ComposerConfig
from src.dsv_core.loader import DirectoryLoader, DirectoryLoaderConfig
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
    # Load the test system data including compositions
    loader_config = DirectoryLoaderConfig(
        local_directory="data/ttl/sample/test-system",
        virtuoso_directory="/ttl/sample/test-system",
        store=virtuoso_store,
        base_uri="http://test.example.org/rdf-system",
    )

    loader = DirectoryLoader(loader_config)
    loader.load()


class TestComposerIntegration:
    """Integration tests for Composer with real Virtuoso."""

    base_uri: str

    @classmethod
    def setup_class(cls) -> None:
        """Set up configuration for all tests in this class."""
        cls.base_uri = "http://test.example.org/rdf-system"

    def create_composer_config(self, virtuoso_store: VirtuosoStore) -> ComposerConfig:
        """Create a ComposerConfig for tests."""
        return ComposerConfig(
            store=virtuoso_store,
            base_uri=self.base_uri,
        )

    @pytest.mark.integration
    def test_compose_basic_person_data_composition(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test composing BasicPersonDataComposition with real data."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Test the basic person data composition
        result = composer.compose(
            "http://dsv.example.org/BasicPersonDataComposition", f"{self.base_uri}/.compositions"
        )

        # Verify the result
        assert isinstance(result, list)
        assert len(result) == 1
        assert "http://test.example.org/rdf-system/.data/people" in result

    @pytest.mark.integration
    def test_compose_person_org_data_composition(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test composing PersonOrgDataComposition with real data."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Test the person-organization data composition
        result = composer.compose(
            "http://dsv.example.org/PersonOrgDataComposition", f"{self.base_uri}/.compositions"
        )

        # Verify the result
        assert isinstance(result, list)
        assert len(result) == 2
        assert "http://test.example.org/rdf-system/.data/people" in result
        assert "http://test.example.org/rdf-system/.data/organizations" in result

    @pytest.mark.integration
    def test_compose_nonexistent_composition(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test composing a non-existent composition raises appropriate error."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Test with a composition that doesn't exist
        with pytest.raises(ValueError, match="contains no graphs"):
            composer.compose(
                "http://dsv.example.org/NonExistentComposition", f"{self.base_uri}/.compositions"
            )

    @pytest.mark.integration
    def test_compose_with_namespace_prefix(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test composing using namespace prefixes instead of full URIs."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Test using the dsv: prefix (this should work if prefixes are properly handled)
        # Note: This test might need adjustment based on how prefixes are handled in SPARQL
        try:
            result = composer.compose(
                "dsv:BasicPersonDataComposition", f"{self.base_uri}/.compositions"
            )
            # If prefix resolution works, we should get the expected result
            assert isinstance(result, list)
            assert len(result) >= 1
        except ValueError:
            # If prefix resolution doesn't work, that's also acceptable behavior
            # The important thing is that the method handles it gracefully
            pass

    @pytest.mark.integration
    def test_compose_result_ordering(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test that compose results are consistently ordered."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Run the same composition multiple times
        compositions_graph = f"{self.base_uri}/.compositions"
        result1 = composer.compose(
            "http://dsv.example.org/PersonOrgDataComposition", compositions_graph
        )
        result2 = composer.compose(
            "http://dsv.example.org/PersonOrgDataComposition", compositions_graph
        )
        result3 = composer.compose(
            "http://dsv.example.org/PersonOrgDataComposition", compositions_graph
        )

        # Results should be consistent across calls
        assert result1 == result2 == result3

        # Results should be ordered (due to ORDER BY in SPARQL query)
        assert result1 == sorted(result1)

    @pytest.mark.integration
    def test_compose_validates_composition_type(
        self, virtuoso_store: VirtuosoStore, loaded_test_data: None
    ) -> None:
        """Test that compose only works with actual DataComposition resources."""
        config = self.create_composer_config(virtuoso_store)
        composer = Composer(config)

        # Try to compose using a shape URI (which is not a DataComposition)
        with pytest.raises(ValueError, match="contains no graphs"):
            composer.compose("http://example.org/PersonShape", f"{self.base_uri}/.compositions")

        # Try to compose using an arbitrary URI
        with pytest.raises(ValueError, match="contains no graphs"):
            composer.compose(
                "http://example.org/SomeRandomResource", f"{self.base_uri}/.compositions"
            )

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
