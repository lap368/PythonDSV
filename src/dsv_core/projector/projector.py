from typing import Any, Dict, List, Optional, Set

from pydantic import BaseModel

from src.dsv_core.store import VirtuosoStore


class ProjectorConfig(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    store: VirtuosoStore
    base_uri: str


class Projector:
    def __init__(self, config: ProjectorConfig) -> None:
        self.config = config
        self.store = config.store
        self.base_uri = config.base_uri

    def project(
        self, graph_uris: List[str], projection_uri: str, projection_graph: str
    ) -> Dict[str, Any]:
        """
        Execute a Shape Projection and return structured data.

        Args:
            graph_uris: The list of graph URIs to project
            projection_uri: The URI of the projection to use
            projection_graph: The graph URI where the projection is defined
        Returns:
            Structured data with entities and their relationships

        Raises:
            ValueError: If the projection is not found or malformed
        """
        # Get all entities that match the main shape
        shape_info = self._get_shape_info(projection_uri, projection_graph)

        # Get base entity URIs first
        base_entity_uris = self._get_base_entity_uris(shape_info, graph_uris)

        # Project the shape recursively starting from these entities
        entities = self._project_shape_recursive(
            projection_uri, base_entity_uris, graph_uris, projection_graph
        )

        return {"entities": entities}

    def _get_shape_info(
        self, projection_uri: str, projection_graph: str, visited_shapes: Optional[Set[str]] = None
    ) -> dict:
        """
        Retrieve shape information from the projection graph, recursively expanding sh:node refs.

        Args:
            projection_uri: The URI of the shape to retrieve
            projection_graph: The graph containing the shape definition
            visited_shapes: Set of already visited shape URIs to prevent infinite recursion

        Returns:
            Dictionary containing target_class and properties information
        """
        if visited_shapes is None:
            visited_shapes = set()

        # Prevent infinite recursion
        if projection_uri in visited_shapes:
            return {"target_class": None, "properties": []}

        visited_shapes.add(projection_uri)

        query = f"""
        PREFIX sh: <http://www.w3.org/ns/shacl#>

        SELECT ?targetClass ?path ?nodeShape WHERE {{
            GRAPH <{projection_graph}> {{
                <{projection_uri}> a sh:NodeShape ;
                                  sh:targetClass ?targetClass .
                OPTIONAL {{
                    <{projection_uri}> sh:property ?prop .
                    ?prop sh:path ?path .
                    OPTIONAL {{
                        ?prop sh:node ?nodeShape .
                    }}
                }}
            }}
        }}
        """

        result = self.store.query(query)

        if not result or "results" not in result or "bindings" not in result["results"]:
            raise ValueError(f"Shape projection '{projection_uri}' not found or query failed")

        bindings = result["results"]["bindings"]
        if not bindings:
            raise ValueError(f"Shape projection '{projection_uri}' not found")

        # Extract target class and properties
        target_class = None
        properties = []

        for binding in bindings:
            if "targetClass" in binding:
                target_class = binding["targetClass"]["value"]

            if "path" in binding:
                prop_info = {
                    "path": binding["path"]["value"],
                    "node_shape": None,
                    "nested_properties": [],
                }

                # If this property has a node shape reference, expand it recursively
                if "nodeShape" in binding and binding["nodeShape"]:
                    node_shape_uri = binding["nodeShape"]["value"]
                    prop_info["node_shape"] = node_shape_uri

                    # Recursively get the referenced shape's properties
                    nested_shape_info = self._get_shape_info(
                        node_shape_uri, projection_graph, visited_shapes.copy()
                    )
                    if nested_shape_info and nested_shape_info.get("properties"):
                        prop_info["nested_properties"] = nested_shape_info["properties"]

                properties.append(prop_info)

        if not target_class:
            raise ValueError(f"Shape projection '{projection_uri}' has no target class")

        return {"target_class": target_class, "properties": properties}

    def _get_shape_info_simple(self, projection_uri: str, projection_graph: str) -> dict:
        """
        Retrieve basic shape information without recursive sh:node expansion.

        Args:
            projection_uri: The URI of the shape to retrieve
            projection_graph: The graph containing the shape definition

        Returns:
            Dictionary containing target_class and properties information
        """
        query = f"""
        PREFIX sh: <http://www.w3.org/ns/shacl#>

        SELECT ?targetClass ?path ?nodeShape WHERE {{
            GRAPH <{projection_graph}> {{
                <{projection_uri}> a sh:NodeShape ;
                                  sh:targetClass ?targetClass .
                OPTIONAL {{
                    <{projection_uri}> sh:property ?prop .
                    ?prop sh:path ?path .
                    OPTIONAL {{
                        ?prop sh:node ?nodeShape .
                    }}
                }}
            }}
        }}
        """

        result = self.store.query(query)

        if not result or "results" not in result or "bindings" not in result["results"]:
            raise ValueError(f"Shape projection '{projection_uri}' not found or query failed")

        bindings = result["results"]["bindings"]
        if not bindings:
            raise ValueError(f"Shape projection '{projection_uri}' not found")

        # Extract target class and properties (without recursive expansion)
        target_class = None
        properties = []

        for binding in bindings:
            if "targetClass" in binding:
                target_class = binding["targetClass"]["value"]

            if "path" in binding:
                prop_info = {
                    "path": binding["path"]["value"],
                    "node_shape": (
                        binding.get("nodeShape", {}).get("value")
                        if "nodeShape" in binding
                        else None
                    ),
                }
                properties.append(prop_info)

        if not target_class:
            raise ValueError(f"Shape projection '{projection_uri}' has no target class")

        return {"target_class": target_class, "properties": properties}

    def _get_base_entity_uris(self, shape_info: dict, graph_uris: List[str]) -> List[str]:
        """
        Get URIs of all entities that match the target class of the shape.

        Args:
            shape_info: Shape information containing target_class
            graph_uris: List of graph URIs to search in

        Returns:
            List of entity URIs
        """
        # If no graphs specified, return empty list
        if not graph_uris:
            return []

        target_class = shape_info["target_class"]

        # Build FROM clauses
        from_clauses = ""
        for graph_uri in graph_uris:
            from_clauses += f"FROM <{graph_uri}>\n"

        query = f"""
        SELECT DISTINCT ?subject
        {from_clauses.rstrip()}
        WHERE {{
            ?subject a <{target_class}> .
        }}
        ORDER BY ?subject
        """

        result = self.store.query(query)
        if not result or "results" not in result:
            return []

        return [binding["subject"]["value"] for binding in result["results"]["bindings"]]

    def _project_shape_recursive(
        self,
        shape_uri: str,
        subject_uris: List[str],
        graph_uris: List[str],
        projection_graph: str,
        visited_shapes: Optional[Set[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Recursively project a shape for given subjects, handling sh:node references.

        Args:
            shape_uri: URI of the shape to project
            subject_uris: List of subject URIs to project
            graph_uris: List of graph URIs containing data
            projection_graph: Graph containing shape definitions
            visited_shapes: Set of visited shapes to prevent cycles

        Returns:
            List of entity dictionaries with nested relationships
        """
        if visited_shapes is None:
            visited_shapes = set()

        # Prevent infinite recursion
        if shape_uri in visited_shapes:
            return []

        if not subject_uris:
            return []

        visited_shapes.add(shape_uri)

        # Get shape information (without recursive expansion - we handle that here)
        shape_info = self._get_shape_info_simple(shape_uri, projection_graph)

        # Get base properties for all subjects
        base_data = self._get_base_properties(shape_info, subject_uris, graph_uris)

        # For each sh:node property, get related entities and recurse
        for prop in shape_info["properties"]:
            if prop.get("node_shape"):
                # Get relationships for this property
                relationships = self._get_relationships(prop, subject_uris, graph_uris)

                # Get unique related entity URIs
                related_uris = list(set(rel["object"] for rel in relationships))

                if related_uris:
                    # Recursively project the referenced shape
                    nested_entities = self._project_shape_recursive(
                        prop["node_shape"],
                        related_uris,
                        graph_uris,
                        projection_graph,
                        visited_shapes.copy(),
                    )

                    # Merge nested entities into base data
                    self._merge_relationships(base_data, relationships, nested_entities, prop)

        return list(base_data.values())

    def _get_base_properties(
        self, shape_info: dict, subject_uris: List[str], graph_uris: List[str]
    ) -> Dict[str, Dict[str, Any]]:
        """
        Get base properties (non-sh:node) for given subjects.

        Returns:
            Dictionary mapping subject URI to entity data
        """
        if not subject_uris:
            return {}

        target_class = shape_info["target_class"]

        # Build VALUES clause for subjects
        values_clause = "VALUES ?subject { " + " ".join(f"<{uri}>" for uri in subject_uris) + " }"

        # Build FROM clauses
        from_clauses = ""
        for graph_uri in graph_uris:
            from_clauses += f"FROM <{graph_uri}>\n"

        # Get simple properties (non-sh:node)
        simple_properties = [
            prop for prop in shape_info["properties"] if not prop.get("node_shape")
        ]

        if not simple_properties:
            # No simple properties, just return subjects with basic structure
            return {uri: {"subject": uri} for uri in subject_uris}

        # Build SELECT variables and OPTIONAL patterns
        select_vars = ["?subject"]
        where_patterns = [f"    ?subject a <{target_class}> ."]
        seen_vars = {"subject"}  # Track unique variables

        for prop in simple_properties:
            var_name = self._get_local_name(prop["path"])
            if var_name not in seen_vars:  # Only add if not already seen
                select_vars.append(f"?{var_name}")
                where_patterns.append(f"    OPTIONAL {{ ?subject <{prop['path']}> ?{var_name} . }}")
                seen_vars.add(var_name)

        query = f"""
        SELECT {' '.join(select_vars)}
        {from_clauses.rstrip()}
        WHERE {{
            {values_clause}
            {chr(10).join(where_patterns)}
        }}
        ORDER BY ?subject
        """

        result = self.store.query(query)
        if not result or "results" not in result:
            return {}

        # Convert to entity dictionaries
        entities = {}
        for binding in result["results"]["bindings"]:
            subject_uri = binding["subject"]["value"]
            entity = {"subject": subject_uri}

            # Add simple properties
            for prop in simple_properties:
                var_name = self._get_local_name(prop["path"])
                if var_name in binding:
                    entity[var_name] = binding[var_name]["value"]

            entities[subject_uri] = entity

        return entities

    def _get_relationships(
        self, prop_info: dict, subject_uris: List[str], graph_uris: List[str]
    ) -> List[Dict[str, str]]:
        """
        Get relationships for a specific sh:node property.

        Returns:
            List of {"subject": uri, "object": uri} relationships
        """
        if not subject_uris:
            return []

        # Build VALUES clause
        values_clause = "VALUES ?subject { " + " ".join(f"<{uri}>" for uri in subject_uris) + " }"

        # Build FROM clauses
        from_clauses = ""
        for graph_uri in graph_uris:
            from_clauses += f"FROM <{graph_uri}>\n"

        query = f"""
        SELECT ?subject ?object
        {from_clauses.rstrip()}
        WHERE {{
            {values_clause}
            ?subject <{prop_info['path']}> ?object .
        }}
        """

        result = self.store.query(query)
        if not result or "results" not in result:
            return []

        return [
            {"subject": binding["subject"]["value"], "object": binding["object"]["value"]}
            for binding in result["results"]["bindings"]
        ]

    def _merge_relationships(
        self,
        base_data: Dict[str, Dict[str, Any]],
        relationships: List[Dict[str, str]],
        nested_entities: List[Dict[str, Any]],
        prop_info: dict,
    ) -> None:
        """
        Merge nested entities into base data based on relationships.
        """
        # Create lookup for nested entities by subject URI
        nested_lookup = {entity["subject"]: entity for entity in nested_entities}

        # Group relationships by subject
        relationships_by_subject = {}
        for rel in relationships:
            subject = rel["subject"]
            if subject not in relationships_by_subject:
                relationships_by_subject[subject] = []
            relationships_by_subject[subject].append(rel["object"])

        # Add relationships to base entities
        prop_name = self._get_local_name(prop_info["path"])

        for subject_uri, entity in base_data.items():
            if subject_uri in relationships_by_subject:
                related_uris = relationships_by_subject[subject_uri]
                related_entities = [
                    nested_lookup[uri] for uri in related_uris if uri in nested_lookup
                ]

                if len(related_entities) == 1:
                    # Single relationship - store as object
                    entity[prop_name] = related_entities[0]
                elif len(related_entities) > 1:
                    # Multiple relationships - store as array
                    entity[prop_name] = related_entities
                # If no related entities found, don't add the property

    def _get_local_name(self, uri: str) -> str:
        """
        Extract the local name from a URI for use as a SPARQL variable.
        """
        if "#" in uri:
            return uri.split("#")[-1]
        elif "/" in uri:
            return uri.split("/")[-1]
        else:
            return uri
