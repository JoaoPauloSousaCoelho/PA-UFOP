# Diminuir para conquistar
import numpy as np

A = np.matrix([[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3],
[1,2,3,4,1,2,3,4],[10,20,3,4,15,12,7,8],[1,2,3,4,22,23,13,14],[0,1,5,6,100,2,1,3]])

def soma(linha):
    sum = 0
    n = len(linha)
    for i in range(n):
        sum += linha[i]
    return sum

n_col = len(A)

soma_total = 0

for j in range(n_col):
    soma_total += soma(A[j,:])