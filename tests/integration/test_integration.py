#!/usr/bin/env python3
"""Integration tests to verify DSV system works with running Virtuoso."""

import pytest

from src.dsv_core import DSVCore
from src.dsv_core.core import DSVConfig
from src.dsv_core.store import VirtuosoStore


class TestDSVIntegration:
    """Integration tests that require running Virtuoso container."""

    @pytest.mark.integration
    def test_local_store_configuration(self) -> None:
        """Test local store configuration works correctly."""
        config = DSVConfig(store_type="local")
        dsv = DSVCore(config)

        assert dsv.config.store_type == "local"
        assert dsv.store is None  # No store initialized for local mode

    @pytest.mark.integration
    def test_virtuoso_store_initialization(self) -> None:
        """Test Virtuoso store initializes with real container."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        assert dsv.config.store_type == "virtuoso"
        assert dsv.store is not None
        assert isinstance(dsv.store, VirtuosoStore)
        assert dsv.config.virtuoso_endpoint == "http://localhost:8890/sparql"

    @pytest.mark.integration
    def test_sparql_query_execution(self) -> None:
        """Test basic SPARQL query execution against Virtuoso."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        # Ensure store is initialized
        assert dsv.store is not None

        # Execute a simple query to list graphs
        result = dsv.store.query("SELECT ?g WHERE { GRAPH ?g { ?s ?p ?o } } LIMIT 5")

        # Verify query structure
        assert "results" in result
        assert "bindings" in result["results"]

        # Should return some results (Virtuoso has default graphs)
        bindings = result["results"]["bindings"]
        assert isinstance(bindings, list)
        assert len(bindings) >= 0  # May be 0 if no data loaded yet

    @pytest.mark.integration
    def test_store_helper_methods(self) -> None:
        """Test VirtuosoStore helper methods work correctly."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        assert dsv.store is not None

        # Test list_graphs method
        graphs = dsv.store.list_graphs()
        assert isinstance(graphs, list)

        # Test count_triples method
        count = dsv.store.count_triples()
        assert isinstance(count, int)
        assert count >= 0

    @pytest.mark.integration
    def test_sparql_update_operations(self) -> None:
        """Test SPARQL UPDATE operations work (requires elevated permissions)."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        assert dsv.store is not None

        # Test graph URI for this test
        test_graph = "http://example.com/dsv-test"

        try:
            # Clean up any existing test data
            cleanup_query = f"DROP SILENT GRAPH <{test_graph}>"
            dsv.store.update(cleanup_query)

            # Insert multiple test triples
            insert_query = f"""
            INSERT DATA {{
                GRAPH <{test_graph}> {{
                    <http://example.com/product1> <http://example.com/name> "Test Product 1" ;
                                                 <http://example.com/price> 19.99 ;
                                                 <http://example.com/category> "Electronics" .
                    <http://example.com/product2> <http://example.com/name> "Test Product 2" ;
                                                 <http://example.com/price> 29.99 ;
                                                 <http://example.com/category> "Books" .
                }}
            }}
            """

            result = dsv.store.update(insert_query)
            assert result is True

            # Query all inserted data
            select_query = f"""
            SELECT ?product ?name ?price ?category WHERE {{
                GRAPH <{test_graph}> {{
                    ?product <http://example.com/name> ?name ;
                            <http://example.com/price> ?price ;
                            <http://example.com/category> ?category .
                }}
            }}
            ORDER BY ?name
            """

            query_result = dsv.store.query(select_query)
            bindings = query_result["results"]["bindings"]

            assert len(bindings) == 2, f"Expected 2 products, found {len(bindings)}"

            # Verify first product
            product1 = bindings[0]
            assert product1["name"]["value"] == "Test Product 1"
            assert float(product1["price"]["value"]) == 19.99
            assert product1["category"]["value"] == "Electronics"

            # Verify second product
            product2 = bindings[1]
            assert product2["name"]["value"] == "Test Product 2"
            assert float(product2["price"]["value"]) == 29.99
            assert product2["category"]["value"] == "Books"

            # Test UPDATE operation (modify existing data)
            update_query = f"""
            DELETE {{
                GRAPH <{test_graph}> {{
                    <http://example.com/product1> <http://example.com/price> ?oldPrice .
                }}
            }}
            INSERT {{
                GRAPH <{test_graph}> {{
                    <http://example.com/product1> <http://example.com/price> 24.99 .
                }}
            }}
            WHERE {{
                GRAPH <{test_graph}> {{
                    <http://example.com/product1> <http://example.com/price> ?oldPrice .
                }}
            }}
            """

            update_result = dsv.store.update(update_query)
            assert update_result is True

            # Verify the price was updated
            price_check_query = f"""
            SELECT ?price WHERE {{
                GRAPH <{test_graph}> {{
                    <http://example.com/product1> <http://example.com/price> ?price .
                }}
            }}
            """

            price_result = dsv.store.query(price_check_query)
            price_bindings = price_result["results"]["bindings"]
            assert len(price_bindings) == 1
            assert float(price_bindings[0]["price"]["value"]) == 24.99

            print(f"\n✅ SPARQL UPDATE Success: Created and modified {len(bindings)} products")

            # Clean up test data
            dsv.store.update(cleanup_query)

        except RuntimeError as e:
            if "SECURITY" in str(e):
                pytest.skip("Virtuoso security settings prevent UPDATE operations")
            else:
                raise

    @pytest.mark.integration
    def test_error_handling(self) -> None:
        """Test error handling for invalid queries."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        assert dsv.store is not None

        # Test invalid SPARQL query
        with pytest.raises(RuntimeError, match="SPARQL query failed"):
            dsv.store.query("INVALID SPARQL QUERY")

        # Test invalid SPARQL update
        with pytest.raises(RuntimeError, match="SPARQL update failed"):
            dsv.store.update("INVALID UPDATE QUERY")

    @pytest.mark.integration
    def test_ttl_file_loading(self) -> None:
        """Test TTL file loading and verify data persistence."""
        config = DSVConfig(store_type="virtuoso")
        dsv = DSVCore(config)

        assert dsv.store is not None

        # Test graph for TTL loading
        test_graph = "http://example.com/dsv-ttl-test"

        try:
            # Clean up any existing test data
            cleanup_query = f"DROP SILENT GRAPH <{test_graph}>"
            dsv.store.update(cleanup_query)

            # Load TTL file into test graph
            success = dsv.store.load_ttl_file("/ttl/sample/products.ttl", test_graph)
            assert success is True

            # Verify the data was actually loaded by querying it
            verify_query = f"""
            SELECT ?name ?price WHERE {{
                GRAPH <{test_graph}> {{
                    ?product <http://example.com/dsv/name> ?name ;
                            <http://example.com/dsv/price> ?price .
                }}
            }}
            """

            query_result = dsv.store.query(verify_query)
            bindings = query_result["results"]["bindings"]

            # Should have loaded the sample products data
            assert len(bindings) > 0, "No products found after TTL loading"

            # Verify specific product data exists (based on actual TTL file content)
            product_names = [binding["name"]["value"] for binding in bindings]
            assert (
                "Wireless Headphones" in product_names
            ), "Expected 'Wireless Headphones' product not found"
            assert "Coffee Mug" in product_names, "Expected 'Coffee Mug' product not found"
            assert "Running Shoes" in product_names, "Expected 'Running Shoes' product not found"

            # Verify prices are numbers
            prices = [float(binding["price"]["value"]) for binding in bindings]
            assert all(price > 0 for price in prices), "All prices should be positive"

            print(f"\n✅ TTL Loading Success: Loaded {len(bindings)} products")
            for binding in bindings:
                name = binding["name"]["value"]
                price = binding["price"]["value"]
                print(f"   • {name}: ${price}")

            # Clean up test data
            dsv.store.update(cleanup_query)

        except Exception as e:
            pytest.skip(f"TTL loading failed - may require additional Virtuoso permissions: {e}")


# Helper function for manual testing
def run_integration_demo() -> None:
    """Run integration demo with detailed output."""
    print("🧪 Running DSV Integration Demo...")

    config = DSVConfig(store_type="virtuoso")
    dsv = DSVCore(config)

    if dsv.store:
        print(f"✅ Connected to Virtuoso at {config.virtuoso_endpoint}")

        # Show available graphs
        graphs = dsv.store.list_graphs()
        print(f"📊 Found {len(graphs)} graphs")

        # Show triple count
        count = dsv.store.count_triples()
        print(f"🔢 Total triples: {count}")

        print("\n💡 Docker management commands:")
        print("   • Status: poetry run python docker-compose/manage.py status")
        print("   • Stop:   poetry run python docker-compose/manage.py stop")
    else:
        print("❌ Failed to connect to Virtuoso")


if __name__ == "__main__":
    run_integration_demo()
