# Soma Dividir para conquistar
import numpy as np 

A = np.matrix([[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3],
[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3]])

def BruteForce(A):
    soma = 0
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            soma += A[i,j]            
    return soma

def split(A):
    n_t = len(A)
    return A[:n_t//2, :n_t//2], A[:n_t//2, n_t//2:], A[n_t//2:, :n_t//2], A[n_t//2:, n_t//2:]

def div_conq_soma(A):
    if len(A)<=2:
        return BruteForce(A)

    a, b, c, d = split(A)
    sum_1 = div_conq_soma(a)
    sum_2 = div_conq_soma(b)  
    sum_3 = div_conq_soma(c)  
    sum_4 = div_conq_soma(d)
    return sum_1 + sum_2+ sum_3 + sum_4   

soma = div_conq_soma(A)
print(f"Soma Algoritmo Dividir e Conquistar: {soma}")