from itertools import permutations
from sys import maxsize

V = 4

def travellingSalesmanPerson(graph, s):
    # store all vertex of traveling Salesman Person
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store the minimum weight Hamilton Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        #Compute the path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight +=graph[k][s]             
        # update minimum
        min_path = min(min_path, current_pathweight) 

    return min_path    

graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]

s = 0
print(travellingSalesmanPerson(graph, s))
