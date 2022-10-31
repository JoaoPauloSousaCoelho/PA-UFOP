# Divide and Conquer - Max value
def MaxValue(arr, l, r, maxval):
    if r == l:
        x = arr[r]
        return x
        
    elif r-l == 1:
        if arr[l]<=arr[r]:
            x = arr[r]
        else:
            x = arr[l]
        return x
                      

    else:
        m = (l+r)//2
        x_1 = MaxValue(arr,l,m, maxval)
        x_2 = MaxValue(arr, m + 1, r, maxval)

    if x_1>x_2:
        return x_1
    else:
        return x_2        
         

arr = [12, 11, 13, 5, 21, 7,50,49,0,12]  
maximovalue = MaxValue(arr, 0, len(arr)-1, 1)
print("Maximum value: ", maximovalue)
