import pytest
from busqueda import buscqueda_lineal, busqueda_binaria_iterativa, busqueda_binaria_recursiva, burbuja

# Pruebas para la búsqueda lineal
def test_buscqueda_lineal():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert buscqueda_lineal(arr, 22) == 4  # El índice de 22 debe ser 4
    assert buscqueda_lineal(arr, 100) == -1  # 100 no está en el arreglo

# Pruebas para la búsqueda binaria iterativa
def test_busqueda_binaria_iterativa():
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr.sort()  # La búsqueda binaria requiere que el arreglo esté ordenado
    assert busqueda_binaria_iterativa(arr, 22) == 3  # 22 debe estar en la posición 3
    assert busqueda_binaria_iterativa(arr, 100) == -1  # 100 no está en el arreglo

# Pruebas para la búsqueda binaria recursiva
def test_busqueda_binaria_recursiva():
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr.sort()  # La búsqueda binaria requiere que el arreglo esté ordenado
    assert busqueda_binaria_recursiva(arr, 22, 0, len(arr) - 1) == 3  # 22 debe estar en la posición 3
    assert busqueda_binaria_recursiva(arr, 100, 0, len(arr) - 1) == -1  # 100 no está en el arreglo

# Pruebas para el algoritmo de burbuja
def test_burbuja():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert burbuja(arr) == [11, 12, 22, 25, 34, 64, 90]  # El arreglo ordenado debe ser así

