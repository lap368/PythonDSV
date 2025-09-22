import os
from pathlib import Path
from typing import List

from pydantic import BaseModel

from .store import VirtuosoStore


class DirectoryLoaderConfig(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    local_directory: str
    virtuoso_directory: str
    store: VirtuosoStore
    base_uri: str


class DirectoryLoader:
    def __init__(self, config: DirectoryLoaderConfig) -> None:
        self.config = config
        self.store = config.store
        self.local_directory = config.local_directory
        self.virtuoso_directory = config.virtuoso_directory

        self.extensions_to_load_functions = {".ttl": self.load_turtle_file}

    def load_turtle_file(self, root: str, ttl_file: str, graph_uri: str) -> bool:

        local_file_path = os.path.join(root, ttl_file)

        # Convert local path to virtuoso path
        # Calculate relative path from local base to current file
        local_abs_path = os.path.abspath(local_file_path)
        local_base_abs = os.path.abspath(self.local_directory)
        relative_path_to_base = os.path.relpath(local_abs_path, local_base_abs)

        # Construct virtuoso path
        virtuoso_file_path = os.path.join(self.virtuoso_directory, relative_path_to_base).replace(
            os.sep, "/"
        )

        try:
            success = self.store.load_ttl_file(virtuoso_file_path, graph_uri)
            if success:
                print(f"✓ Loaded {ttl_file} into graph: {graph_uri}")
                return True
            else:
                print(f"✗ Failed to load {ttl_file}")
                return False
        except Exception as e:
            print(f"✗ Error loading {ttl_file}: {e}")
            return False

    def load(self) -> List[str]:
        """Load all supported files from the directory recursively.

        Files in the same directory get loaded into the same named graph.
        The graph URI is constructed as: base_uri/[relative_path_to_parent_dir]
        Supported file types are determined by the extensions_to_load_functions mapping.

        Returns:
            List of graph URIs that were loaded
        """
        loaded_graphs: list[str] = []
        base_path = Path(self.local_directory).resolve()
        extensions = self.extensions_to_load_functions.keys()

        for root, _, files in os.walk(self.local_directory):
            # Find all files in current directory with the supported extensions
            supported_files = [f for f in files if Path(f).suffix.lower() in extensions]

            if not supported_files:
                continue

            # Calculate relative path from base directory to current directory
            current_path = Path(root).resolve()
            relative_path = current_path.relative_to(base_path)

            # Construct graph URI: base_uri/relative_path
            if str(relative_path) == ".":
                # Root directory case
                graph_uri = self.config.base_uri.rstrip("/")
            else:
                # Convert path separators to forward slashes for URI
                path_str = str(relative_path).replace(os.sep, "/")
                graph_uri = f"{self.config.base_uri.rstrip('/')}/{path_str}"

            # Load all supported files from this directory into the same graph
            directory_loaded = False
            for file in supported_files:
                file_extension = Path(file).suffix.lower()
                load_function = self.extensions_to_load_functions[file_extension]
                if load_function(root, file, graph_uri):
                    directory_loaded = True

            # Add the graph URI only once per directory if any files were loaded
            if directory_loaded:
                loaded_graphs.append(graph_uri)

        return loaded_graphs
