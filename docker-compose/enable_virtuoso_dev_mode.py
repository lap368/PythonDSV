#!/usr/bin/env python3
"""
Manual script to enable Virtuoso development mode with full permissions.
Run this after starting Virtuoso to enable SPARQL updates and file loading.
"""

import subprocess
import time
import sys


def run_isql_command(sql_command):
    """Run an ISQL command against the Virtuoso container."""
    cmd = ["docker", "exec", "-i", "dsv-virtuoso", "isql", "1111", "dba", "dba"]

    try:
        process = subprocess.run(cmd, input=sql_command, text=True, capture_output=True, timeout=30)

        if process.returncode == 0:
            return True, process.stdout
        else:
            return False, process.stderr

    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def enable_dev_mode():
    """Enable development mode permissions in Virtuoso."""
    print("🔧 Enabling Virtuoso development mode...")

    # Check if container is running
    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", "name=dsv-virtuoso", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
        )
        if "dsv-virtuoso" not in result.stdout:
            print("❌ Virtuoso container is not running!")
            print("   Start it with: poetry run python docker-compose/manage.py start --wait")
            return False
    except Exception as e:
        print(f"❌ Error checking container status: {e}")
        return False

    print("✅ Virtuoso container is running")

    # Wait a moment for Virtuoso to be fully ready
    print("⏳ Waiting for Virtuoso to be ready...")
    time.sleep(5)

    # SQL commands to enable development permissions
    sql_commands = [
        # Grant SPARQL_UPDATE role to SPARQL user
        'GRANT SPARQL_UPDATE TO "SPARQL";',
        # Grant specific procedure permissions
        'GRANT EXECUTE ON DB.DBA.SPARUL_LOAD TO "SPARQL";',
        'GRANT EXECUTE ON DB.DBA.SPARUL_DROP TO "SPARQL";',
        'GRANT EXECUTE ON DB.DBA.SPARUL_CLEAR TO "SPARQL";',
        'GRANT EXECUTE ON DB.DBA.SPARUL_INSERT TO "SPARQL";',
        'GRANT EXECUTE ON DB.DBA.SPARUL_DELETE TO "SPARQL";',
        # Set default permissions for graphs
        "DB.DBA.RDF_DEFAULT_USER_PERMS_SET('nobody', 7);",
        "DB.DBA.RDF_DEFAULT_USER_PERMS_SET('SPARQL', 15);",
        # Commit changes
        "COMMIT WORK;",
    ]

    print("🔐 Setting up permissions...")

    success_count = 0
    for i, cmd in enumerate(sql_commands, 1):
        print(f"   [{i}/{len(sql_commands)}] {cmd[:50]}...")

        success, output = run_isql_command(cmd)
        if success:
            success_count += 1
            print(f"      ✅ Success")
        else:
            print(f"      ⚠️  Warning: {output.strip()}")

    print(f"\n📊 Results: {success_count}/{len(sql_commands)} commands succeeded")

    if success_count >= len(sql_commands) - 2:  # Allow a few warnings
        print("✅ Development mode enabled successfully!")
        print("\n🧪 You can now test with:")
        print("   poetry run pytest tests/test_integration.py -m integration -v")
        return True
    else:
        print("⚠️  Some commands failed, but basic functionality may still work")
        return False


def test_permissions():
    """Test if the permissions are working."""
    print("\n🧪 Testing permissions...")

    import sys
    from pathlib import Path

    # Add the project root to the path so we can import from src
    sys.path.insert(0, str(Path(__file__).parent.parent))

    from src.dsv_core import DSVCore
    from src.dsv_core.core import DSVConfig

    config = DSVConfig(store_type="virtuoso")
    dsv = DSVCore(config)

    if not dsv.store:
        print("❌ Failed to connect to Virtuoso")
        return False

    # Test simple insert
    test_graph = "http://example.com/permission-test"

    try:
        # Try to insert some test data
        insert_query = f"""
        INSERT DATA {{
            GRAPH <{test_graph}> {{
                <http://example.com/test> <http://example.com/label> "Permission test successful" .
            }}
        }}
        """

        result = dsv.store.update(insert_query)
        if result:
            print("✅ SPARQL UPDATE permissions working!")

            # Clean up
            cleanup_query = f"DROP SILENT GRAPH <{test_graph}>"
            dsv.store.update(cleanup_query)

            return True
        else:
            print("❌ SPARQL UPDATE still not working")
            return False

    except Exception as e:
        print(f"❌ SPARQL UPDATE test failed: {e}")
        return False


if __name__ == "__main__":
    success = enable_dev_mode()

    if success:
        test_permissions()

    print("\n💡 Next steps:")
    print("   • Run integration tests: poetry run pytest tests/test_integration.py -m integration")
    print("   • Check status: poetry run python docker-compose/manage.py status")
    print("   • View logs: poetry run python docker-compose/manage.py logs")
