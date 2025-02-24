from app.division import divide
import pytest
def test_division():
    assert divide(10,2)== 5;
    assert divide(6,2)==3;

    pass

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        assert divide(4,0)==0
        pass