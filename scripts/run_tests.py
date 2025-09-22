#!/usr/bin/env python3
"""Test runner script for DSV project."""

import argparse
import subprocess
import sys


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n🔄 {description}")
    print(f"Running: {' '.join(cmd)}")
    print("-" * 50)

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ {description} - PASSED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED (exit code: {e.returncode})")
        return False


def main() -> None:
    """Main test runner."""
    parser = argparse.ArgumentParser(description="Run DSV tests")
    parser.add_argument(
        "--type",
        choices=["unit", "integration", "all"],
        default="all",
        help="Type of tests to run (default: all)",
    )
    parser.add_argument("--coverage", action="store_true", help="Run tests with coverage reporting")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--failfast", "-x", action="store_true", help="Stop on first failure")

    args = parser.parse_args()

    # Base command
    base_cmd = ["poetry", "run", "pytest"]

    # Add options
    if args.verbose:
        base_cmd.append("-v")
    if args.failfast:
        base_cmd.append("-x")
    if args.coverage:
        base_cmd.extend(["--cov=src", "--cov-report=term-missing"])

    success = True

    if args.type == "unit" or args.type == "all":
        # Run unit tests
        unit_cmd = base_cmd + ["tests/unit/"]
        success &= run_command(unit_cmd, "Unit Tests")

    if args.type == "integration" or args.type == "all":
        # Run integration tests
        integration_cmd = base_cmd + ["tests/integration/", "-m", "integration"]
        success &= run_command(integration_cmd, "Integration Tests")

    if args.type == "all":
        # Run all tests together for final summary
        all_cmd = base_cmd + ["tests/"]
        success &= run_command(all_cmd, "All Tests Summary")

    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
