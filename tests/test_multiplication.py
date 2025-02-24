"""Unit tests for the multiplication function."""
from app.multiplication import multiply

def test_addition():
    """Test that multiplication() correctly multiplies two numbers."""
    assert multiply(5, 2) == 10
    assert multiply(-1, 4) == -4
    assert multiply(0, 0) == 0
