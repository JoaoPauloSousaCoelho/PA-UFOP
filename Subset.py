def subsetUtil(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):
        #include the A[i] element in subset
        subset.append(A[i])

        #move onto the next element
        subsetUtil(A, subset, i + 1)

        #exclude the A[i] element from subset and triggers backtracking 
        subset.pop(-1)
    return


# below function returns the subsets of a vector
def subsets(A):
    global res 
    subset = []

    #keeps track of current element in vector A
    index = 0
    subsetUtil(A, subset, index)

array = [1,2,2,3,4]

subsets(array)