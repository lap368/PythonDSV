#!/usr/bin/env python3
"""Example demonstrating the DirectoryLoader functionality."""

import os

from dsv_core.loader import DirectoryLoader, DirectoryLoaderConfig
from dsv_core.stores import StoreConfig, VirtuosoStore


def main() -> None:
    """Demonstrate loading TTL files from a directory structure."""

    # Configuration for Virtuoso store (adjust as needed)
    store_config = StoreConfig(
        endpoint_url="http://localhost:8890/sparql", username="dba", password="dba"
    )

    # Create store instance
    store = VirtuosoStore(store_config)

    # Paths for RDF system directory
    local_rdf_system_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "ttl", "rdf-system"
    )
    virtuoso_rdf_system_path = "/ttl/rdf-system"

    # Create loader configuration
    loader_config = DirectoryLoaderConfig(
        local_directory=local_rdf_system_path,
        virtuoso_directory=virtuoso_rdf_system_path,
        store=store,
        base_uri="http://example.org/rdf-system",
    )

    # Create and use the loader
    loader = DirectoryLoader(loader_config)

    print(f"Loading TTL files from: {local_rdf_system_path} -> {virtuoso_rdf_system_path}")
    print(f"Base URI: {loader_config.base_uri}")
    print("-" * 50)

    try:
        loaded_graphs = loader.load()

        print("-" * 50)
        print(f"Successfully loaded {len(loaded_graphs)} graph(s):")
        for graph_uri in loaded_graphs:
            print(f"  - {graph_uri}")

        # Optional: Show some statistics
        print("\nGraph statistics:")
        for graph_uri in loaded_graphs:
            count = store.count_triples(graph_uri)
            print(f"  {graph_uri}: {count} triples")

    except Exception as e:
        print(f"Error during loading: {e}")


if __name__ == "__main__":
    main()
