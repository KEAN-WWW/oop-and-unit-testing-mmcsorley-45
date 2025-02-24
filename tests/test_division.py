"""Unit tests for the division function."""
import pytest
from app.division import divide

def test_division():
    """Test that divide() correctly divides two numbers."""
    assert divide(10,2)== 5
    assert divide(6,2)==3

def test_divide_zero_exception():
    """Test 0 output"""
    with pytest.raises(ZeroDivisionError):
        assert divide(4,0)==0
