
# Task-1
def k_core(adj_matrix, k):
    # Initializing variables
    deg = list()
    rem = set()
    flag = True

    # Degree is a list containing the degrees of each node.
    # It is calculated by adding the col elements of each row in the adjacency matrix.
    for i in range(len(adj_matrix)):
        deg.append(sum(adj_matrix[i]))

    # rem is a set containing indices of elements from adj matrix with degrees < k.
    # The elements in rem need to be removed from the graph.
    for i in range(len(adj_matrix)):
        if deg[i] < k:
           rem.add(i)

    # Iteratively removing elements from adjacency matrix that are present in rem.
    while True:
        if not rem:
            return adj_matrix
        
        v = rem.pop()
        deg[v] = 0
        for i in range(len(adj_matrix)):
            if adj_matrix[v][i]:
                if deg[i] > 0:
                    deg[i] -= 1
                if deg[i] < k and deg[i] != 0:
                    rem.add(i)
        
        print(deg)

        core = list()
        for i in range(len(deg)):
            if deg[i] >= k:
                core.append(i)

        # If core is empty, we halt.
        # Otherwise, if any degree is less than k, we continue the algorithm.
        # Else return the core matrix.   
        if not core:
            print("The k-core is empty at k=", k)
            return core
        else:
            for i in range(len(deg)):
                if deg[i] < k:
                    flag = False

        if flag == True:    
            core_matrix = [[adj_matrix[i][j] for j in core] for i in core]
            return core_matrix
    

# Task-2
def matrix_from_sequence(bit_seq):
    curr = 0
    adj_matrix = [[0 for _ in range(27)] for _ in range(27)]
    for i in range(27):
        for j in range(27):
            adj_matrix[i][j] = int(bit_seq[curr])
            curr += 1

    # Eliminate isolated nodes by setting first and last column and row to 1.
    for i in range(27):
        if sum(adj_matrix[i]) == 0:
            adj_matrix[i][0] = 1
            adj_matrix[i][-1] = 1
            adj_matrix[0][i] = 1
            adj_matrix[-1][i] = 1

    # Replace main diagonal entries with 0.
    for i in range(27):
        adj_matrix[i][i] = 0

    # Make matrix symmetric by swapping (i,j) and (j,i) for i<j.
    for i in range(27):
        for j in range(i):
            adj_matrix[i][j], adj_matrix[j][i] = adj_matrix[j][i], adj_matrix[i][j]
    
    return adj_matrix
    

# Task-3
# Calling the matrix_from_sequence function with UTD ID bit sequence.
bit_seq = "0001100101" * 73
adj_matrix = matrix_from_sequence(bit_seq)

# Using values of k=1,2,3... on the returned value on k_core function till it keeps
# returning non-empty cores.
k = 1
while True:
    core_matrix = k_core(adj_matrix, k)
    if not core_matrix:
        break
    else:
        print("k-core with k=", k)
        print(core_matrix)
        k += 1
