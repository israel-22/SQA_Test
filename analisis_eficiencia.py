
import time
import numpy as np  # type: ignore
from itertools import permutations


#rdenamiento por busqueda lineal
def get_first_element(arr):
    return arr[0]


#rdenamiento por busqueda lineal
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#rdenamiento por busqueda binaria
def busqueda_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

#rdenamiento por bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        
#rdenamiento por merge
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
            

def get_first_element(arr):
    return arr[0]


def buscqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1   

def busqueda_binaria(arr, x):
    low = 0
    high= len(arr)-1

    while low <= high:
     mid = (low + high) // 2
    if arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        high = mid - 1
    else:
      return mid

    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#rdenamiento por merge
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
np.random.seed(42) # esta semilla define un valor caso contreario es un dato aleatorio
arr= np.random.randint(1, 100, size=10000) 


#Complejidad constante 
inicio=time.time()
print(get_first_element(arr)) 
fin= time.time()

print(f"Tiempo de ejecución constante: {fin-inicio} segundos") 

#complejidad Lineal

inicio=time.time()
print(buscqueda_lineal(arr, 42)) 
fin= time.time()

print(f"Tiempo de ejecución Lineal: {fin-inicio} segundos")

#Complejidad Logaritmica
inicio=time.time()
print(buscqueda_lineal(arr, 42)) 
fin= time.time()

print(f"Tiempo de ejecución Logaritmica: {fin-inicio} segundos")

#Complejidad Cuadratica
arr= np.random.randint(1, 100, size=10000) 
inicio=time.time()
bubble_sort(arr)
print(arr) 
fin= time.time()
print(f"Tiempo de ejecución Bubble Sort: {fin-inicio} segundos")

#Complegidad Logaritmica

arr= np.random.randint(1, 100, size=10000) 
inicio=time.time()
merge_sort(arr)
print(arr) 
fin= time.time()
print(f"Tiempo de ejecución Merge Sort: {fin-inicio} segundos")

#Complejidad Exponencial
inicio=time.time()
print(busqueda_binaria(arr, 42)) 
fin= time.time()

print(f"Tiempo de ejecución Exponencial: {fin-inicio} segundos")

          
#rdenamiento por fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#rdenamiento por selection sort
def all_permutations(arr):
    return list(permutations(arr))

np.random.seed(42)
arr = np.random.randint(1, 100, size=100)

#rdenamiento por selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(arr)
        arr[i], arr[min_idx] = arr[j+1], arr[i]
        return arr
    
    
#rdenamiento por selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
          min_idx = i
    for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
             min_idx = j
            print(arr)  
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            return arr   
        
#rdenamiento por insertion sort O(n^2)
def insertion_sort(arr):
    n = len(arr)
    print (arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]: 
            arr[j+1]=arr[j]
            j-=1
            print(arr)
        arr[j+1]=key        
        return arr
        
        
# Complejidad constante
inicio = time.time()
print(get_first_element(arr))
fin = time.time()
print(f"Tiempo de ejecución (complejidad constante): {fin - inicio} segundos")

# Complejidad lineal
inicio = time.time()
print(busqueda_lineal(arr, 42))
fin = time.time()
print(f"Tiempo de ejecución (complejidad lineal): {fin - inicio} segundos")

# Complejidad logarítmica
inicio = time.time()
arr.sort()
print(busqueda_binaria(arr, 42))
fin = time.time()
print(f"Tiempo de ejecución (complejidad logarítmica): {fin - inicio} segundos")

# Complejidad cuadrática
arr = [64, 35, 25, 12, 22, 11, 90]
inicio = time.time()
bubble_sort(arr)
print(arr)
fin = time.time()
print(f"Tiempo de ejecución (complejidad cuadrática): {fin - inicio} segundos")

# Complejidad log-lineal
inicio = time.time()
merge_sort(arr)
print(arr)
fin = time.time()
print(f"Tiempo de ejecución (complejidad log-lineal): {fin - inicio} segundos")

# Complejidad exponencial
inicio = time.time()
print(fibonacci(38))
fin = time.time()
print(f"Tiempo de ejecución (complejidad exponencial): {fin - inicio} segundos")

# Complejidad factorial
inicio = time.time()
print(all_permutations([1, 2, 3]))
fin = time.time()
print(f"Tiempo de ejecución (complejidad factorial): {fin - inicio} segundos")

# Complejidad selection sort
inicio = time.time()
print(selection_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución (complejidad selection sort): {fin - inicio} segundos")

# Complejidad insertion sort
inicio = time.time()
print(insertion_sort(arr))
fin = time.time()
print(f"Tiempo de ejecución (complejidad insertion sort): {fin - inicio} segundos")
