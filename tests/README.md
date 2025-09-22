# DSV Test Suite

This directory contains the test suite for the DSV (Data-Shape-View) system, organized into unit and integration tests.

## Test Structure

```
tests/
├── unit/                           # Unit tests (no external dependencies)
│   ├── test_core.py               # DSV core functionality tests
│   ├── test_directory_loader.py   # Directory loader tests (mocked)
│   ├── test_environment.py        # Environment configuration tests
│   └── test_virtuoso_store.py     # Store configuration tests
├── integration/                    # Integration tests (require external services)
│   ├── test_integration.py        # General system integration tests
│   └── test_directory_loader_integration.py  # Directory loader with real Virtuoso
└── README.md                      # This file
```

## Test Categories

### Unit Tests (`tests/unit/`)
- **No external dependencies** - Use mocks and stubs
- **Fast execution** - Run in milliseconds
- **Isolated** - Test individual components in isolation
- **Always runnable** - No setup requirements

### Integration Tests (`tests/integration/`)
- **Require external services** - Need running Virtuoso instance
- **Slower execution** - May take seconds to complete
- **End-to-end testing** - Test complete workflows
- **Setup required** - Need Docker containers or external services

## Running Tests

### Quick Commands

```bash
# Run all tests
poetry run pytest

# Run only unit tests (fast)
poetry run pytest tests/unit/

# Run only integration tests (requires Virtuoso)
poetry run pytest tests/integration/ -m integration

# Run specific test file
poetry run pytest tests/unit/test_directory_loader.py -v
```

### Using the Test Runner Script

```bash
# Run all tests with coverage
python scripts/run_tests.py --coverage

# Run only unit tests
python scripts/run_tests.py --type unit

# Run only integration tests
python scripts/run_tests.py --type integration

# Verbose output with fail-fast
python scripts/run_tests.py --verbose --failfast
```

### Test Markers

Tests are marked with pytest markers:

- `@pytest.mark.unit` - Unit tests (no external dependencies)
- `@pytest.mark.integration` - Integration tests (require external services)
- `@pytest.mark.slow` - Slow tests (may be skipped in CI)

```bash
# Run only unit tests
poetry run pytest -m "unit"

# Run all except integration tests
poetry run pytest -m "not integration"

# Run all except slow tests
poetry run pytest -m "not slow"
```

## Integration Test Requirements

Integration tests require:

1. **Running Virtuoso instance** on `localhost:8890`
2. **Default credentials** (`dba`/`dba`)
3. **SPARQL endpoint** accessible at `http://localhost:8890/sparql`

### Starting Virtuoso for Testing

```bash
# Using Docker Compose (recommended)
cd docker-compose/virtuoso
docker-compose up -d

# Verify Virtuoso is running
curl http://localhost:8890/sparql
```

## Test Data

Integration tests use:
- **Temporary directories** with generated TTL files
- **Sample RDF data** representing shapes, views, ontologies, and tenant data
- **Realistic directory structures** matching the expected rdf-system layout

## Coverage

Run tests with coverage reporting:

```bash
# Generate coverage report
poetry run pytest --cov=src --cov-report=html --cov-report=term-missing

# View HTML coverage report
open htmlcov/index.html
```

## Continuous Integration

For CI environments:

```bash
# Run unit tests only (no external dependencies)
poetry run pytest tests/unit/ --cov=src

# Run integration tests (requires setup)
# 1. Start Virtuoso container
# 2. Wait for service to be ready
# 3. Run integration tests
poetry run pytest tests/integration/ -m integration
```

## Writing New Tests

### Unit Tests
- Place in `tests/unit/`
- Use mocks for external dependencies
- Test individual functions/classes in isolation
- Should run in < 100ms each

### Integration Tests  
- Place in `tests/integration/`
- Mark with `@pytest.mark.integration`
- Use real external services
- Test complete workflows
- Clean up resources in teardown methods

### Example Unit Test
```python
def test_my_function():
    """Test my_function with mocked dependencies."""
    with patch('module.external_service') as mock_service:
        mock_service.return_value = "expected_result"
        result = my_function()
        assert result == "expected_result"
```

### Example Integration Test
```python
@pytest.mark.integration
def test_my_workflow(virtuoso_store):
    """Test complete workflow with real Virtuoso."""
    # Use real store, real data
    result = complete_workflow(virtuoso_store)
    assert result.success
    # Clean up in teardown
```
