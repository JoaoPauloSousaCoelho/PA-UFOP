# Insertion Sort

A = [89,45,68,90,29,34,17]

n = len(A)

for i in range(1,n):
    v = A[i]
    j = i - 1

    while j>=0 and A[j] > v:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = v    

print(A)   