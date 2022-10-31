# fake coin
import numpy as np 
def find_fake_coin(A):
    n = len(A)
    r = n
    l = 0  
    peso = sum(A)/2 
    
    while (l<=r and r != 0):       
        m = np.int64((l+r)/2)
        delta = np.average(A[l:m]) - np.average(A[m:r])               
        if((delta != 0 and len(A[l:m])==0) or (delta != 0 and len(A[m:r])==0)):
            if(m==0):
                return -1
            else:              
                return m

        elif (delta>0):
            #r = m - 1
            l = m

        elif(np.isnan(delta)):
            return -1    

        else:
             r = m
                  

    return -1

A = [4,4,4,4,4,4,4,4,0,4,4,4]              
indice = find_fake_coin(A)