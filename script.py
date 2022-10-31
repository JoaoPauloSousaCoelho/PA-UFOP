import numpy as np

def n_permutacao(n):
    aux = 1
    for i in range(0,n):
        aux = aux*(i+1)
    return aux  


def montar_direcao(n):
    dir = []
    for i in range(0,n):
        dir.append(-1)
    return dir

def swap(v,i,j):
    aux = v
    temp = aux[i]
    aux[i] = aux[j]
    aux[j] = temp
    return aux

direcao = montar_direcao(4)
n_fatorial = n_permutacao(4)    

v = list(range(1,5))
n = len(v)
i = len(v)-1
j = 0
n_fatorial = n_permutacao(4)
count = 0
#while count<=n_fatorial:
#    i_max = np.argmax(v[j:n])
#    mobile = np.max(v[j:n])
#    #print(mobile)
#    if(mobile>v[i]):
#        v = swap(v,i_max,i_max-1)
#        print(v)
#    i = i-1
#    #print(n)
#    if(i<0):
#        i = len(v)-1
#        j = j + 1
#    if(j==n):
#        break     
#    count = count + 1

def find_maior(v,inicio,n):
    aux = 0
    for j in range(inicio, n):
        if(aux<v[j]):
            aux = v[j]
            indice = j
    return aux, indice   

v = list(range(1,5))
count = 0
n = len(v)
for i in range(0, len(v)-1):
    flag = True
    while flag:
        mobile,indice = find_maior(v,i,n)
        #print(indice)    
        v = swap(v,indice,indice-1)        
        print(v)
        if(indice-1==i):
            flag = False
        count = count + 1

n = len(v)-1
limite = n
for i in range(0, len(v)-1):
    flag = True
    while flag:
        mobile,indice = find_maior(v,0,limite)
        #print(indice)    
        v = swap(v,indice,indice+1)        
        print(v)
        if(indice+1<=n):
            flag = False
            #limite = limite - 1
        count = count + 1        
    #print(count)    
