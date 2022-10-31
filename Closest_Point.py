# Closest Point
import numpy as np

ncol = d.shape[0]
nrow = d.shape[1]
min = np.Inf

Y = [1,2,3,4]
X = [2,3,4,5]

def distancia(X,Y):
    n = len(X)
    d = np.zeros(shape = (n,n))
    for i in range(0, n):
        for j in range(i+1, n):
            d[i,j] = np.power(X[j] - X[i],2) + np.power(Y[j] - Y[i],2)
    return d  


def distancia_minima(d):
    aux = np.Inf
    for i in range(0,ncol):
        for j in range(i+1, nrow):
            if(d[i,j]<aux):
                aux = d[i,j]
    return aux            


matriz_distancia = distancia(X,Y)
minima_distancia = distancia_minima(matriz_distancia)
print(minima_distancia)