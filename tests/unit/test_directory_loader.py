"""Tests for DirectoryLoader functionality."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

from src.dsv_core.loader import DirectoryLoader, DirectoryLoaderConfig
from src.dsv_core.store import VirtuosoStore


class TestDirectoryLoader:
    """Test cases for DirectoryLoader."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_store = MagicMock(spec=VirtuosoStore)
        self.mock_store.load_ttl_file.return_value = True

    def test_directory_loader_config(self) -> None:
        """Test DirectoryLoaderConfig creation."""
        config = DirectoryLoaderConfig(
            local_directory="/test/path",
            virtuoso_directory="/ttl/test/path",
            store=self.mock_store,
            base_uri="http://example.org/test",
        )

        assert config.local_directory == "/test/path"
        assert config.virtuoso_directory == "/ttl/test/path"
        assert config.store == self.mock_store
        assert config.base_uri == "http://example.org/test"

    def test_directory_loader_init(self) -> None:
        """Test DirectoryLoader initialization."""
        config = DirectoryLoaderConfig(
            local_directory="/test/path",
            virtuoso_directory="/ttl/test/path",
            store=self.mock_store,
            base_uri="http://example.org/test",
        )

        loader = DirectoryLoader(config)

        assert loader.local_directory == "/test/path"
        assert loader.virtuoso_directory == "/ttl/test/path"
        assert loader.store == self.mock_store
        assert loader.config == config

    def test_load_single_directory_with_ttl_files(self) -> None:
        """Test loading TTL files from a single directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test TTL files
            ttl_file1 = Path(temp_dir) / "test1.ttl"
            ttl_file2 = Path(temp_dir) / "test2.ttl"
            non_ttl_file = Path(temp_dir) / "readme.txt"

            ttl_file1.write_text("@prefix ex: <http://example.org/> .")
            ttl_file2.write_text("@prefix ex: <http://example.org/> .")
            non_ttl_file.write_text("This is not a TTL file")

            config = DirectoryLoaderConfig(
                local_directory=temp_dir,
                virtuoso_directory=f"/ttl{temp_dir}",
                store=self.mock_store,
                base_uri="http://example.org/test",
            )

            loader = DirectoryLoader(config)

            with patch("builtins.print"):  # Suppress print statements
                loaded_graphs = loader.load()

            # Should load 2 TTL files into 1 graph (same directory)
            assert len(loaded_graphs) == 1
            assert loaded_graphs[0] == "http://example.org/test"

            # Should call load_ttl_file twice (once for each TTL file)
            assert self.mock_store.load_ttl_file.call_count == 2

    def test_load_nested_directories(self) -> None:
        """Test loading TTL files from nested directories."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create nested directory structure
            shapes_dir = Path(temp_dir) / "shapes"
            views_dir = Path(temp_dir) / "views"
            ontologies_dir = Path(temp_dir) / "ontologies"

            shapes_dir.mkdir()
            views_dir.mkdir()
            ontologies_dir.mkdir()

            # Create TTL files in different directories
            (shapes_dir / "person.ttl").write_text("@prefix ex: <http://example.org/> .")
            (shapes_dir / "organization.ttl").write_text("@prefix ex: <http://example.org/> .")
            (views_dir / "person_view.ttl").write_text("@prefix ex: <http://example.org/> .")
            (ontologies_dir / "core.ttl").write_text("@prefix ex: <http://example.org/> .")

            config = DirectoryLoaderConfig(
                local_directory=temp_dir,
                virtuoso_directory=f"/ttl{temp_dir}",
                store=self.mock_store,
                base_uri="http://example.org/test",
            )

            loader = DirectoryLoader(config)

            with patch("builtins.print"):  # Suppress print statements
                loaded_graphs = loader.load()

            # Should create 3 graphs (one for each subdirectory)
            assert len(loaded_graphs) == 3

            expected_graphs = {
                "http://example.org/test/shapes",
                "http://example.org/test/views",
                "http://example.org/test/ontologies",
            }
            assert set(loaded_graphs) == expected_graphs

            # Should call load_ttl_file 4 times (once for each TTL file)
            assert self.mock_store.load_ttl_file.call_count == 4

    def test_load_with_root_directory_files(self) -> None:
        """Test loading TTL files from root directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create TTL file in root directory
            root_ttl = Path(temp_dir) / "root.ttl"
            root_ttl.write_text("@prefix ex: <http://example.org/> .")

            # Create subdirectory with TTL file
            sub_dir = Path(temp_dir) / "subdir"
            sub_dir.mkdir()
            (sub_dir / "sub.ttl").write_text("@prefix ex: <http://example.org/> .")

            config = DirectoryLoaderConfig(
                local_directory=temp_dir,
                virtuoso_directory=f"/ttl{temp_dir}",
                store=self.mock_store,
                base_uri="http://example.org/test",
            )

            loader = DirectoryLoader(config)

            with patch("builtins.print"):  # Suppress print statements
                loaded_graphs = loader.load()

            # Should create 2 graphs (root and subdirectory)
            assert len(loaded_graphs) == 2

            expected_graphs = {
                "http://example.org/test",  # root directory
                "http://example.org/test/subdir",  # subdirectory
            }
            assert set(loaded_graphs) == expected_graphs

    def test_load_handles_store_errors(self) -> None:
        """Test that loader handles store errors gracefully."""
        self.mock_store.load_ttl_file.side_effect = Exception("Store error")

        with tempfile.TemporaryDirectory() as temp_dir:
            ttl_file = Path(temp_dir) / "test.ttl"
            ttl_file.write_text("@prefix ex: <http://example.org/> .")

            config = DirectoryLoaderConfig(
                local_directory=temp_dir,
                virtuoso_directory=f"/ttl{temp_dir}",
                store=self.mock_store,
                base_uri="http://example.org/test",
            )

            loader = DirectoryLoader(config)

            with patch("builtins.print"):  # Suppress print statements
                loaded_graphs = loader.load()

            # Should return empty list when all loads fail
            assert loaded_graphs == []

    def test_load_skips_directories_without_ttl_files(self) -> None:
        """Test that loader skips directories without TTL files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create directories with non-TTL files
            empty_dir = Path(temp_dir) / "empty"
            txt_dir = Path(temp_dir) / "txt_only"

            empty_dir.mkdir()
            txt_dir.mkdir()
            (txt_dir / "readme.txt").write_text("Not a TTL file")

            config = DirectoryLoaderConfig(
                local_directory=temp_dir,
                virtuoso_directory=f"/ttl{temp_dir}",
                store=self.mock_store,
                base_uri="http://example.org/test",
            )

            loader = DirectoryLoader(config)

            with patch("builtins.print"):  # Suppress print statements
                loaded_graphs = loader.load()

            # Should return empty list (no TTL files found)
            assert loaded_graphs == []
            assert self.mock_store.load_ttl_file.call_count == 0
