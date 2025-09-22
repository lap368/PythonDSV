from typing import List

from pydantic import BaseModel

from src.dsv_core.store import VirtuosoStore


class ComposerConfig(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    store: VirtuosoStore
    base_uri: str

    # Eventually, this will also include the scope of the composition


class Composer:
    def __init__(self, config: ComposerConfig) -> None:
        self.config = config
        self.store = config.store
        self.base_uri = config.base_uri

    def compose(self, composition_uri: str, composition_graph: str) -> List[str]:
        """
        Retrieve a Data Composition and return the list of graph URIs it includes.

        Args:
            composition_uri: The URI of the Data Composition to retrieve
            composition_graph: The graph URI where the composition is defined

        Returns:
            List of graph URIs included in the composition

        Raises:
            ValueError: If the composition is not found or malformed
        """
        # SPARQL query to extract the list of graphs from the composition
        # Use Virtuoso-compatible syntax for RDF list traversal with explicit graph
        query = f"""
        PREFIX dsv: <http://dsv.example.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT ?graph WHERE {{
            GRAPH <{composition_graph}> {{
                <{composition_uri}> dsv:includesGraphs ?list .
                ?list rdf:rest* ?node .
                ?node rdf:first ?graph .
            }}
        }}
        ORDER BY ?graph
        """

        # Execute the query
        result = self.store.query(query)

        # Extract graph URIs from the result
        if not result or "results" not in result or "bindings" not in result["results"]:
            raise ValueError(f"Composition '{composition_uri}' not found or query failed")

        bindings = result["results"]["bindings"]
        if not bindings:
            raise ValueError(f"Composition '{composition_uri}' contains no graphs")

        # Extract the graph URIs
        graph_uris = []
        for binding in bindings:
            if "graph" in binding and "value" in binding["graph"]:
                graph_uris.append(binding["graph"]["value"])

        if not graph_uris:
            raise ValueError(f"Composition '{composition_uri}' has malformed graph list")

        return graph_uris
