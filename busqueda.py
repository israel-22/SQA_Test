#busqueda lineal
def buscqueda_lineal(arr, x):
    for i in range(len(arr)):
        print (i, arr[i],x)
        if arr[i] == x:
            return i    
    return -1 

#busqueda binaria iterativa
def busqueda_binaria_iterativa(arr, x):
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
        print(low,mid,high)
    return -1

def busqueda_binaria_recursiva(arr, x, left, right):
    if left > right: return -1
    mid = (left + right) // 2
    if arr[mid] == x: return mid
    elif arr[mid] < x:
        return busqueda_binaria_recursiva(arr, x, mid + 1, right)
    else:
        return busqueda_binaria_recursiva(arr, x, left, mid -1 )
    

#busqueda binaria recursiva
arr = [64, 34, 25, 12, 22, 11, 90]
print(buscqueda_lineal(arr, 22))
arr.sort()
print(busqueda_binaria_iterativa(arr, 22))
print(busqueda_binaria_recursiva(arr, 22, 0, len(arr) - 1))


