"""Unit tests for the subtraction function."""
from app.subtraction import subtract

def test_addition():
    """Test addition of two positive numbers."""
    assert subtract(5, 3) == 2

    assert subtract(-5, 2) == -7

    assert subtract(0, 0) == 0
