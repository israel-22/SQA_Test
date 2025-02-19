import pytest
from calculadora import suma, division

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_suma(a, b, esperado):
    assert suma(a, b) == esperado

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(1, 1) == 1
    with pytest.raises(ValueError):
        division(10, 0)