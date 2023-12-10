from sage.graphs.graph_plot import GraphPlot
from sage.numerical.mip import MixedIntegerLinearProgram
from sage.graphs.graph_generators import graphs

def analyze_graph(a, b, k):
    print(f"k={k}")
    sys.stdout.flush()
    print()
    sys.stdout.flush()
    c1 = graphs.CycleGraph(a)
    c2 = graphs.CycleGraph(b)

    g = c1.cartesian_product(c2)
    show(g)

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


    # Get all vertices in the graph
    vertices = g.vertices()


    # Sort the vertices in ascending order
    vertices = sorted(vertices, key=lambda x: int(x))
    print (vertices)
    print()
    # Initialize an empty matrix to store the distances
    distance_matrix = []

    # Create the distance matrix based on the condition
    for v1 in vertices:
        for v2 in vertices:
            if v1 < v2:
                row = []
                for s in vertices:
                    #print ("par(", v1, ",", v2, "): ", "g.distance(", s, ",", v1, "): ", g.distance(s, v1))
                    #print ("par(", v1, ",", v2, "): ", "g.distance(", s, ",", v2, "): ", g.distance(s, v2))
                    if g.distance(s, v1) != g.distance(s, v2):
                        row.append(1)
                    else:
                        row.append(0)
                distance_matrix.append(row)
                print(f"({v1}, {v2}):", row)
                #print ()

    #print (distance_matrix)

    # Print the resulting distance matrix
    print()
    sys.stdout.flush()
    for i, row in enumerate(distance_matrix):
        v1, v2 = vertices[i // (len(vertices) - 1)], vertices[i % (len(vertices) - 1)]
        print(f"({v1}, {v2}):", row)
    print()

    matrix = distance_matrix

    result = minimal_set_of_columns(matrix, k)
    print("Minimal set(s) of columns:", result)
    sys.stdout.flush()

    dimension = float('inf')
    for i in result:
        if len(i) < dimension:
            dimension = len(i)

    return dimension  # Assuming you want to return the 'dimension' value

# Example usage:
a_value = 2
b_value = 3
k_value = 2
analyze_graph(a_value, b_value, k_value)
