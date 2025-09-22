#!/usr/bin/env python3
"""Simple Docker management script for DSV Virtuoso container."""

import sys
import argparse
import subprocess
from pathlib import Path

# Add the project root to the path so we can import from docker
sys.path.insert(0, str(Path(__file__).parent.parent))

from docker_utils import DockerManager


def enable_dev_mode():
    """Enable Virtuoso development mode by running the dev mode script."""
    script_path = Path(__file__).parent / "enable_virtuoso_dev_mode.py"

    try:
        result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Development mode enabled successfully")
            return True
        else:
            print(f"❌ Failed to enable development mode: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Error enabling development mode: {e}")
        return False


def main():
    """Main function for Docker management CLI."""
    parser = argparse.ArgumentParser(description="Manage DSV Virtuoso Docker container")
    parser.add_argument(
        "action",
        choices=["start", "stop", "restart", "status", "logs", "dev-mode"],
        help="Action to perform",
    )
    parser.add_argument(
        "--wait", "-w", action="store_true", help="Wait for health check when starting"
    )
    parser.add_argument(
        "--enable-dev",
        "-d",
        action="store_true",
        help="Automatically enable development mode after starting",
    )

    args = parser.parse_args()

    # Initialize Docker manager
    manager = DockerManager()

    if args.action == "start":
        print("Starting Virtuoso container...")
        if manager.start_virtuoso(wait_for_health=args.wait):
            print("✅ Virtuoso started successfully")
            if args.wait:
                print("🔍 Health check passed")

            # Enable development mode if requested
            if args.enable_dev:
                print("\n🔧 Enabling development mode...")
                if not enable_dev_mode():
                    print("⚠️  Container started but development mode failed")
                    sys.exit(1)
        else:
            print("❌ Failed to start Virtuoso")
            sys.exit(1)

    elif args.action == "stop":
        print("Stopping Virtuoso container...")
        if manager.stop_virtuoso():
            print("✅ Virtuoso stopped successfully")
        else:
            print("❌ Failed to stop Virtuoso")
            sys.exit(1)

    elif args.action == "restart":
        print("Restarting Virtuoso container...")
        if manager.restart_virtuoso():
            print("✅ Virtuoso restarted successfully")
        else:
            print("❌ Failed to restart Virtuoso")
            sys.exit(1)

    elif args.action == "status":
        if not manager.is_docker_available():
            print("❌ Docker is not available")
            sys.exit(1)

        running = manager.is_virtuoso_running()
        healthy = manager.is_virtuoso_healthy()

        print(f"Container running: {'✅' if running else '❌'}")
        print(f"Health check: {'✅' if healthy else '❌'}")

        info = manager.get_container_info()
        if info:
            print(f"Container ID: {info['id'][:12]}")
            print(f"Image: {info['image']}")
            print(f"Status: {info['status']}")
            print(f"Ports: {info['ports']}")
        else:
            print("No container information available")

    elif args.action == "logs":
        print("Opening container logs...")
        import os

        os.system("docker-compose -f docker-compose/virtuoso/docker-compose.yml logs -f")

    elif args.action == "dev-mode":
        print("🔧 Enabling Virtuoso development mode...")
        if not manager.is_virtuoso_running():
            print("❌ Virtuoso container is not running")
            print("   Start it first with: python manage.py start --wait")
            sys.exit(1)

        if not enable_dev_mode():
            sys.exit(1)


if __name__ == "__main__":
    main()
