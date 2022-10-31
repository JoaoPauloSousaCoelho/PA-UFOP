# Multiplicação de Matriz - Força Bruta
import numpy as np

#A = np.matrix([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
#B = np.matrix([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

A = np.matrix([[1,2,3],[3,4,5],[3,4,5]])
B = np.matrix([[1,2,3],[3,4,5],[3,4,5]])

def BruteForce(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0]*p for i in range(n)])
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i,j] += A[i,k]*B[k,j]
    return C

BruteForce(A,B)