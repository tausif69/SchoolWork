#  File: MST.py

#  Description: Determine the sum of edge weights in a maximal spanning tree

#  Student Name: 

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 

# Find set of vertex i
def find(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i
 
# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j, parent):
    a = find(i, parent)
    b = find(j, parent)
    parent[a] = b
 

# Input: matrix is a 2d square list of integer elements representing edge weights; 0 represents a nonexistent edge
# Output: return the sum of edge weights of the maximal spanning tree
def mst_edge_sum(matrix):
    V = len(matrix)
    parent = [i for i in range(V)]

    max_cost = 0 # Cost of min MST
 
    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i
 
    # Include maximum weight edges one by one
    edge_count = 0
    while edge_count < V - 1:
        max_val = 0
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i, parent) != find(j, parent) and matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    a = i
                    b = j
        union(a, b, parent)
        # print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, max_val))
        edge_count += 1
        max_cost += max_val
 
    return max_cost

def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to mst_edge_sum()
    result = mst_edge_sum(matrix)

    # print the result to standard output
    print(result)


if __name__ == "__main__":
    main()