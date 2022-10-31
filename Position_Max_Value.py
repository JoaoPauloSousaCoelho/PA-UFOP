# Divide and Conquer - Position of Maximum Value
def PositionMaxValue(arr, l, r, maxval):
    if r == l:
        x_min = r
        x_max = r
        return x_min, x_max
        
    elif r-l == 1:
        if arr[l]<=arr[r]:
            x_max = r
            x_min = l
        else:
            x_max = l
            x_min = r

        return x_min, x_max                      

    else:
        m = (l+r)//2
        x_min_1, x_max_1 = PositionMaxValue(arr,l,m, maxval)
        x_min_2, x_max_2 = PositionMaxValue(arr, m + 1, r, maxval)

    if arr[x_min_1]<arr[x_min_2]:
        x_min = x_min_1
    else:
        x_min = x_min_2

    if arr[x_max_1]<arr[x_max_2]:
        x_max = x_max_2
    else:
        x_max = x_max_1

    return x_min, x_max   
     
arr = [12,12,12,12,12,12]  
min, max = PositionMaxValue(arr, 0, len(arr)-1, 1)
print(f"Minimo {min}\nMaximo: {max}")