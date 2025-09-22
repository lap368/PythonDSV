"""Store interfaces for different RDF backends."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel
from SPARQLWrapper import GET, JSON, POST, SPARQLWrapper


class StoreConfig(BaseModel):
    """Base configuration for RDF stores."""

    endpoint_url: str
    username: Optional[str] = None
    password: Optional[str] = None
    default_graph: Optional[str] = None


class VirtuosoStore:
    """Simple SPARQL wrapper interface for Virtuoso.

    Provides a clean interface for executing SPARQL queries against
    a Virtuoso triplestore, whether local Docker or remote AWS instance.
    """

    def __init__(self, config: StoreConfig) -> None:
        """Initialize Virtuoso store with configuration.

        Args:
            config: Store configuration including endpoint URL and credentials
        """
        self.config = config
        self.sparql = SPARQLWrapper(config.endpoint_url)

        # Set up authentication if provided
        if config.username and config.password:
            self.sparql.setCredentials(config.username, config.password)

        # Set default return format
        self.sparql.setReturnFormat(JSON)

    def query(self, sparql_query: str) -> Dict[str, Any]:
        """Execute a SPARQL SELECT query.

        Args:
            sparql_query: SPARQL query string

        Returns:
            Query results as dictionary
        """
        self.sparql.setQuery(sparql_query)
        self.sparql.setMethod(GET)

        try:
            results = self.sparql.query().convert()
            # Ensure we return a dictionary
            if isinstance(results, dict):
                return results
            else:
                return {"error": "Unexpected result type", "raw_result": str(results)}
        except Exception as e:
            raise RuntimeError(f"SPARQL query failed: {e}") from e

    def update(self, sparql_update: str) -> bool:
        """Execute a SPARQL UPDATE query.

        Args:
            sparql_update: SPARQL UPDATE query string

        Returns:
            True if successful
        """
        self.sparql.setQuery(sparql_update)
        self.sparql.setMethod(POST)

        try:
            self.sparql.query()
            return True
        except Exception as e:
            raise RuntimeError(f"SPARQL update failed: {e}") from e

    def load_ttl_file(self, file_path: str, graph_uri: Optional[str] = None) -> bool:
        """Load a TTL file into the triplestore.

        Args:
            file_path: Path to the TTL file
            graph_uri: Optional named graph URI

        Returns:
            True if successful
        """
        graph_clause = f"INTO GRAPH <{graph_uri}>" if graph_uri else ""

        # Use Virtuoso's LOAD command to import TTL file
        load_query = f"""
        LOAD <file://{file_path}> {graph_clause}
        """

        return self.update(load_query.strip())

    def list_graphs(self) -> List[str]:
        """List all named graphs in the triplestore.

        Returns:
            List of graph URIs
        """
        query = """
        SELECT DISTINCT ?g WHERE {
            GRAPH ?g { ?s ?p ?o }
        }
        ORDER BY ?g
        """

        results = self.query(query)
        graphs = []

        for binding in results.get("results", {}).get("bindings", []):
            if "g" in binding:
                graphs.append(binding["g"]["value"])

        return graphs

    def count_triples(self, graph_uri: Optional[str] = None) -> int:
        """Count triples in the store or a specific graph.

        Args:
            graph_uri: Optional graph URI to count triples in

        Returns:
            Number of triples
        """
        if graph_uri:
            query = f"""
            SELECT (COUNT(*) as ?count) WHERE {{
                GRAPH <{graph_uri}> {{ ?s ?p ?o }}
            }}
            """
        else:
            query = """
            SELECT (COUNT(*) as ?count) WHERE {
                ?s ?p ?o
            }
            """

        results = self.query(query)
        bindings = results.get("results", {}).get("bindings", [])

        if bindings and "count" in bindings[0]:
            return int(bindings[0]["count"]["value"])

        return 0
