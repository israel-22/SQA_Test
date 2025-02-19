import time
#rdenamiento por fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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
        

# ORDENAMIENTO POR BURBUJA
def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr

#ORDENAMIENTO POR SELECCIÓN
def selection_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            print(arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ordenamiento por inserción
def insertion_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        print(arr)
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    print(arr)
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print (left, right)
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
            
# ORDENAMIENTO POR QUICK SORT            
def quick_sort(arr):
    n = len(arr)
    if len(arr) <= 1: return arr
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print (left, middle, right)
    return quick_sort(left)+ middle + quick_sort(right)  

         
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