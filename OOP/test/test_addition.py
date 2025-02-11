from app.addition import add

def test_addition():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0