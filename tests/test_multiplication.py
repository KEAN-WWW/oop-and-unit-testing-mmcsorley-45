from app.multiplication import multiply

def test_addition():
    # Test addition of two positive numbers
    assert multiply(5, 2) == 10;

    # Test addition of a negative and a positive number
    assert multiply(-1, 4) == -4;
    # Test addition of two zeros
    assert multiply(0, 0) == 0;

    # Test addition of large numbers