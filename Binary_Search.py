# Binary Search
import numpy as np
def binarySearch(A,K):
    n = len(A)
    l = 0
    r = n-1
    while l<=r:
        m = np.int32((l + r)/2)
        if K == A[m]:
            return m
        elif K< A[m]:
            r = m - 1
        else:
            l = m + 1
    return - 1            

A = [1,2,3,100,200,300,4000]

position = binarySearch(A, 4000)
position