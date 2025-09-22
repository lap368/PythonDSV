# Cursor IDE Test Integration Troubleshooting

## The Problem
You're not seeing the play buttons (▶️) next to test functions in Cursor.

## Step-by-Step Fix

### 1. Restart Cursor Completely
- Close Cursor entirely
- Reopen Cursor and open this project folder

### 2. Set the Python Interpreter
- Press `Cmd+Shift+P` (or `Ctrl+Shift+P` on Windows)
- Type "Python: Select Interpreter"
- Choose: `/Users/lucypatton/Library/Caches/pypoetry/virtualenvs/dsv-jVfODfY3-py3.13/bin/python`

### 3. Configure Tests
- Press `Cmd+Shift+P`
- Type "Python: Configure Tests"
- Select "pytest"
- Select the root directory (should be current folder)
- When asked for arguments, just press Enter (use defaults)

### 4. Refresh Test Discovery
- Press `Cmd+Shift+P`
- Type "Python: Refresh Tests"
- Wait for it to complete

### 5. Check Test View
- Press `Cmd+Shift+P`
- Type "Test: Focus on Test Explorer View"
- You should see a test panel on the left side

### 6. Manual Test Discovery Check
- Open `tests/test_core.py`
- Press `Cmd+Shift+P`
- Type "Test: Discover Tests"

### 7. Alternative: Use Command Palette
If play buttons still don't appear:
- Press `Cmd+Shift+P`
- Type "Test: Run All Tests" to run all tests
- Type "Test: Run Test at Cursor" to run the test your cursor is on

## Debugging Commands

Run these in the terminal to verify everything works:

```bash
# Test that Poetry environment is active
poetry run python -c "import sys; print(sys.executable)"

# Test that pytest can discover tests
poetry run pytest --collect-only

# Run a specific test
poetry run pytest tests/test_core.py::test_dsv_core_initialization -v

# Run all tests
poetry run pytest -v
```

## Common Issues

### Issue 1: Wrong Python Interpreter
**Symptom**: Tests don't run or imports fail
**Fix**: Make sure Cursor is using the Poetry virtual environment path shown above

### Issue 2: Test Discovery Fails
**Symptom**: No tests found
**Fix**:
- Check that `pytest.ini` exists in project root
- Verify `tests/` directory has `__init__.py`
- Run `poetry run pytest --collect-only` to see if pytest can find tests

### Issue 3: Import Errors
**Symptom**: Tests fail with import errors
**Fix**:
- Make sure `src/` is in Python path (check `.vscode/settings.json`)
- Verify all `__init__.py` files exist

## Alternative: Use Tasks Instead

If test discovery still doesn't work, you can use the configured tasks:
- Press `Cmd+Shift+P`
- Type "Tasks: Run Task"
- Select from:
  - "DSV: Run Tests" (all tests)
  - "DSV: Run Unit Tests" (unit tests only)
  - "DSV: Run Integration Tests" (integration tests only)

## Verification

After following these steps, you should see:
1. ▶️ Play buttons next to test functions in `tests/test_core.py`
2. Test results in the Test Explorer panel
3. Ability to run individual tests by clicking the play buttons

If you're still having issues, try opening the workspace file:
- File → Open Workspace
- Select `dsv.code-workspace`
