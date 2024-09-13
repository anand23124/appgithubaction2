from src.math_operation import add,sub

def test_add():
    assert add(5, 3) == 8
    assert add(5, -1) == 4

def test_sub():
    assert sub(5, 3) == 2
    assert sub(5, -1) == 6
    assert sub(-1,-4) == 3
    assert sub(4,4) == 0