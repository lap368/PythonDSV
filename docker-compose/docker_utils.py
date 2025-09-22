"""Docker lifecycle management utilities for Virtuoso.

This module handles Docker container lifecycle management, keeping Docker
operations separate from the core DSV functionality.
"""

import os
import time
import logging
from pathlib import Path
from typing import Optional, Dict, Any, Union
import docker  # type: ignore
import requests
from docker.errors import DockerException, NotFound  # type: ignore


logger = logging.getLogger(__name__)


class DockerManager:
    """Manages Docker lifecycle for Virtuoso container."""

    def __init__(
        self,
        compose_path: str = "docker-compose/virtuoso/docker-compose.yml",
        project_name: str = "dsv",
        health_check_url: str = "http://localhost:8890/sparql",
        startup_timeout: int = 120,
        shutdown_timeout: int = 30,
    ):
        """Initialize Docker manager.

        Args:
            compose_path: Path to docker-compose.yml file
            project_name: Docker Compose project name
            health_check_url: URL to check if Virtuoso is healthy
            startup_timeout: Seconds to wait for startup
            shutdown_timeout: Seconds to wait for shutdown
        """
        self.compose_path = Path(compose_path)
        self.project_name = project_name
        self.health_check_url = health_check_url
        self.startup_timeout = startup_timeout
        self.shutdown_timeout = shutdown_timeout

        try:
            self.client: Optional[Any] = docker.from_env()  # type: ignore
        except DockerException as e:
            logger.error(f"Failed to connect to Docker: {e}")
            self.client = None

    def is_docker_available(self) -> bool:
        """Check if Docker is available and running."""
        if not self.client:
            return False

        try:
            self.client.ping()
            return True
        except DockerException:
            return False

    def is_virtuoso_running(self) -> bool:
        """Check if Virtuoso container is running."""
        if not self.client:
            return False

        try:
            container = self.client.containers.get("dsv-virtuoso")
            return bool(container.status == "running")
        except NotFound:
            return False
        except DockerException as e:
            logger.error(f"Error checking container status: {e}")
            return False

    def is_virtuoso_healthy(self) -> bool:
        """Check if Virtuoso is responding to HTTP requests."""
        try:
            response = requests.get(self.health_check_url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def start_virtuoso(self, wait_for_health: bool = True) -> bool:
        """Start Virtuoso container using docker-compose.

        Args:
            wait_for_health: Whether to wait for health check to pass

        Returns:
            True if started successfully
        """
        if not self.is_docker_available():
            logger.error("Docker is not available")
            return False

        if self.is_virtuoso_running():
            logger.info("Virtuoso is already running")
            if wait_for_health:
                return self._wait_for_health()
            return True

        try:
            # Change to compose directory and run docker-compose up
            compose_dir = self.compose_path.parent
            original_cwd = os.getcwd()

            try:
                os.chdir(compose_dir)
                result = os.system(f"docker-compose -p {self.project_name} up -d")

                if result != 0:
                    logger.error("Failed to start Virtuoso with docker-compose")
                    return False

                logger.info("Virtuoso container started")

                if wait_for_health:
                    return self._wait_for_health()

                return True

            finally:
                os.chdir(original_cwd)

        except Exception as e:
            logger.error(f"Error starting Virtuoso: {e}")
            return False

    def stop_virtuoso(self) -> bool:
        """Stop Virtuoso container using docker-compose.

        Returns:
            True if stopped successfully
        """
        if not self.is_docker_available():
            logger.error("Docker is not available")
            return False

        if not self.is_virtuoso_running():
            logger.info("Virtuoso is not running")
            return True

        try:
            compose_dir = self.compose_path.parent
            original_cwd = os.getcwd()

            try:
                os.chdir(compose_dir)
                result = os.system(f"docker-compose -p {self.project_name} down")

                if result != 0:
                    logger.error("Failed to stop Virtuoso with docker-compose")
                    return False

                logger.info("Virtuoso container stopped")
                return True

            finally:
                os.chdir(original_cwd)

        except Exception as e:
            logger.error(f"Error stopping Virtuoso: {e}")
            return False

    def restart_virtuoso(self) -> bool:
        """Restart Virtuoso container.

        Returns:
            True if restarted successfully
        """
        logger.info("Restarting Virtuoso...")
        if not self.stop_virtuoso():
            return False

        # Wait a moment before restarting
        time.sleep(2)

        return self.start_virtuoso()

    def get_container_info(self) -> Optional[Dict[str, Any]]:
        """Get information about the Virtuoso container.

        Returns:
            Container information dictionary or None
        """
        if not self.client:
            return None

        try:
            container = self.client.containers.get("dsv-virtuoso")
            return {
                "id": container.id,
                "name": container.name,
                "status": container.status,
                "image": (
                    container.image.tags[0]
                    if container.image and container.image.tags
                    else "unknown"
                ),
                "ports": container.ports,
                "created": container.attrs["Created"],
                "started": container.attrs["State"].get("StartedAt"),
            }
        except NotFound:
            return None
        except DockerException as e:
            logger.error(f"Error getting container info: {e}")
            return None

    def _wait_for_health(self) -> bool:
        """Wait for Virtuoso to become healthy.

        Returns:
            True if healthy within timeout
        """
        logger.info(f"Waiting for Virtuoso to become healthy (timeout: {self.startup_timeout}s)")

        start_time = time.time()
        while time.time() - start_time < self.startup_timeout:
            if self.is_virtuoso_healthy():
                elapsed = time.time() - start_time
                logger.info(f"Virtuoso is healthy (took {elapsed:.1f}s)")
                return True

            time.sleep(2)

        logger.error(f"Virtuoso failed to become healthy within {self.startup_timeout}s")
        return False
