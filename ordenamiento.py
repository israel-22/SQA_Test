import time

# Función Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ordenamiento por selección
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ordenamiento por inserción
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Ordenamiento por burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ordenamiento por mezcla (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr  # Se agrega return para devolver la lista ordenada

# Ordenamiento rápido (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


         
#PRUEBAS
arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(bubble_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución bubble sort: {fin - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(selection_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución selection sort: {fin - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(insertion_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución inserción sort: {fin - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(merge_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución inserción sort: {fin - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(quick_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución inserción sort: {fin - inicio} segundos")