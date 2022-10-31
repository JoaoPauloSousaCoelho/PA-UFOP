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
# Strassen's Method

def split(matrix):
    n = len(matrix)
    return matrix[:n//2, :n//2], matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[:n//2, :n//2] 

def strassen(A,B):
    if len(A)<=2:
        return BruteForce(A,B)

    a, b, c, d = split(A)
    e,f,g,h = split(B)
    ae = strassen(a,e)
    bg = strassen(b,g)
    af = strassen(a,f)
    bh = strassen(b,h)
    ce = strassen(c,e)
    dg = strassen(d,g)
    cf = strassen(c,f)
    dh = strassen(d,h)

    C11 = ae + bg
    C12 = af + bh
    C21 = ce + dg
    C22 = cf + dh

    C = np.vstack((np.hstack((C11,C12)), np.hstack((C21,C22))))

    return C

A = np.matrix([[1,2,3,4],[3,4,5,6],[3,4,5,6],[3,4,5,6]])
B = np.matrix([[1,2,3,4],[3,4,5,6],[3,4,5,6],[3,4,5,6]])

C = strassen(A,B)
print(C)