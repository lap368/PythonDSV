"""Core DSV engine for RDF Data-Shape-View operations."""

import logging
import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from rdflib import Graph

from .store import StoreConfig, VirtuosoStore

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


class DSVConfig(BaseModel):
    """Configuration for DSV system."""

    # Core settings
    store_type: str = Field(default_factory=lambda: os.getenv("DSV_STORE_TYPE", "local"))
    store_path: Optional[str] = Field(default_factory=lambda: os.getenv("DSV_STORE_PATH"))
    base_uri: str = Field(
        default_factory=lambda: os.getenv("DSV_BASE_URI", "https://example.com/dsv/")
    )

    # Virtuoso-specific settings
    virtuoso_endpoint: str = Field(
        default_factory=lambda: os.getenv("DSV_VIRTUOSO_ENDPOINT", "http://localhost:8890/sparql")
    )
    virtuoso_username: Optional[str] = Field(
        default_factory=lambda: os.getenv("DSV_VIRTUOSO_USERNAME", "dba")
    )
    virtuoso_password: Optional[str] = Field(
        default_factory=lambda: os.getenv("DSV_VIRTUOSO_PASSWORD", "dba")
    )
    default_graph: Optional[str] = Field(default_factory=lambda: os.getenv("DSV_DEFAULT_GRAPH"))

    # Development settings
    debug: bool = Field(default_factory=lambda: os.getenv("DSV_DEBUG", "false").lower() == "true")
    log_level: str = Field(default_factory=lambda: os.getenv("DSV_LOG_LEVEL", "INFO"))


class DSVCore:
    """Core DSV engine for RDF Data-Shape-View operations.

    This is the main entry point for the DSV system, handling:
    - RDF data management
    - Shape validation and projection
    - View resolution and inheritance
    """

    def __init__(self, config: DSVConfig) -> None:
        """Initialize DSV core with configuration."""
        self.config = config
        self.graph = Graph()
        self.store: Optional[VirtuosoStore] = None

        # Set up logging
        logging.basicConfig(level=getattr(logging, config.log_level.upper()))

        # Initialize store based on configuration
        if config.store_type == "virtuoso":
            self._initialize_virtuoso_store()

    def _initialize_virtuoso_store(self) -> None:
        """Initialize Virtuoso store."""
        # Create store configuration
        store_config = StoreConfig(
            endpoint_url=self.config.virtuoso_endpoint,
            username=self.config.virtuoso_username,
            password=self.config.virtuoso_password,
            default_graph=self.config.default_graph,
        )

        try:
            self.store = VirtuosoStore(store_config)
            logger.info("Virtuoso store initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Virtuoso store: {e}")
            self.store = None
