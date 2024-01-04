import sys
from sage.all import *
from sage.graphs.graph_plot import GraphPlot
from sage.numerical.mip import MixedIntegerLinearProgram

def minimal_set_of_columns(matrix, k):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    dp = [0] * (1 << num_cols)
    col_indices = [-1] * (1 << num_cols)
    min_set = []

    for mask in range(1 << num_cols):
        total_sum = [0] * num_rows

        for j in range(num_cols):
            if mask & (1 << j):
                for i in range(num_rows):
                    total_sum[i] += matrix[i][j]

        valid = True
        for i in range(num_rows):
            if total_sum[i] < k:
                valid = False
                break

        if valid:
            dp[mask] = bin(mask).count('1')

            col_indices[mask] = [j for j in range(num_cols) if mask & (1 << j)]

            if len(min_set) == 0 or dp[mask] < dp[min_set[0]]:
                min_set = [mask]
            elif dp[mask] == dp[min_set[0]]:
                min_set.append(mask)

    return [set(col_indices[mask]) for mask in min_set]


def dimenzija_poti(k, a, b, c):

    Pa = graphs.PathGraph(a)
    Pb = graphs.PathGraph(b)
    Pc = graphs.PathGraph(c)


    g1 = Pa.cartesian_product(Pb)
    g = g1.cartesian_product(Pc)

    # Get all vertices in the graph
    vertices = g.vertices()



    # Initialize an empty matrix to store the distances
    distance_matrix = []

    # Create the distance matrix based on the condition
    for v1 in vertices:
        for v2 in vertices:
            if v1 < v2:
                row = []
                for s in vertices:
                    if g.distance(s, v1) != g.distance(s, v2):
                        row.append(1)
                    else:
                        row.append(0)
                distance_matrix.append(row)


    matrix = distance_matrix

    result = minimal_set_of_columns(matrix, k)

    dimension = float('inf')
    for i in result:
        if len(i) < dimension:
            dimension = len(i)

    print("(a=", a, ", b=", b, ", c=", c, ", k=", k, ", dim=", dimension, ")")


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
k = int(sys.argv[4])
dimenzija_poti(k, a, b, c)
