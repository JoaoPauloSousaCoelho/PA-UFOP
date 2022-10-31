import numpy as np
# Sequential Search
def sequential_search(A,number):
    for i in range(0, A.size):
        if(A[i] == number):
            return i
    return -1        

A = np.array([19,10,9,5,4,3,2,23,8,90,100,87])
number = 23

indice = sequential_search(A,5)