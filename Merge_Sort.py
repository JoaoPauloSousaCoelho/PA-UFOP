# MergeSort
def MergeSort(arr):
    if len(arr)>1:
        # Fiding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        MergeSort(L)

        # Sorting the second half
        MergeSort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i]<=R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1 
            k += 1

        #Checking if any element was left

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1    

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
MergeSort(arr)

print(arr)