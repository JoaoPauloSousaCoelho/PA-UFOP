import numpy as np

# Selection Sort
def swap(vector,min,j):
    aux = vector[min]
    vector[min] = vector[j]
    vector[j] = aux
    return vector

A = np.array([19,10,9,5,4,3,2,23,8,90,100,87])
n = A.size

for i in range(0,n):
    min = i
    for j in range(i+1,n):
        if(A[j]<A[min]):
            min = j
    B = swap(A, min, i) 


    