import numpy as np

A = np.matrix([[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3],
[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3]])
n = A.shape[0]-1

def BruteForce(A):
    soma = 0
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            soma += A[i,j]            
    return soma

soma = BruteForce(A)
print(f"Soma Algoritmo Força Bruta: {soma}")