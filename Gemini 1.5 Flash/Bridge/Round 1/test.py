import pytest

# ... (your test functions here)

# Ensure 100% branch coverage with Pytest
def test_branch_coverage():
    pytest.main(["-v", "--cov", "your_module"])