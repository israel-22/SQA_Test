import pytest
from ordenamiento import (
    fibonacci,
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

# Pruebas para Fibonacci
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

# Pruebas para algoritmos de ordenamiento
@pytest.mark.parametrize("sorting_function", [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
])
def test_sorting_algorithms(sorting_function):
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(arr)  # Lo que debería ser el resultado
    assert sorting_function(arr[:]) == expected  # Se pasa una copia de la lista
