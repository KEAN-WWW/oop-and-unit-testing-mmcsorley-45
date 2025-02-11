from app.addition import add

def test_addition():
    result = add( 2, 2)
    if result == 4:
       pass
    result = add(2,2)
    assert result ==4
