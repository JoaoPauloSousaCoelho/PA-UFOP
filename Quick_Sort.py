# QuickSort Algorithm

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def QuickSort(arr, low, high):
    if(low<high):
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

def Partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    for j in range(low, high):
        pivot = arr[high]
        if(arr[j]<pivot):
            i = i+1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1
    
arr = [7, 2, 1, 6, 8, 5, 3, 4]
n = len(arr)

QuickSort(arr, 0, n-1)
print("Ordened array: ", arr)                   