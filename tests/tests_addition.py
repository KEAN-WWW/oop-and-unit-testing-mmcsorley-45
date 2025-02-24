"""Unit tests for the addition function."""
from app.addition import add

def test_addition():
    """Test addition of two positive numbers."""
    assert add(2, 2) == 4

    # Test addition of a negative and a positive number
    assert add(-1, 1) == 0

    # Test addition of two zeros
    assert add(0, 0) == 0
