from app.subtraction import subtract

def test_addition():
    # Test addition of two positive numbers
    assert subtract(5, 3) == 2;

    # Test addition of a negative and a positive number
    assert subtract(-5, 2) == -7;

    # Test addition of two zeros
    assert subtract(0, 0) == 0;
