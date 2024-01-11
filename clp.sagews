from sage.graphs.graph_plot import GraphPlot
from sage.numerical.mip import MixedIntegerLinearProgram

def CLP_k_dim(g, k_value):
    # Ustvarimo CLP
    p = MixedIntegerLinearProgram(maximization=False)
    # Nove spremenljivke
    x = p.new_variable(binary=True)
    # Ciljna funkcija
    p.set_objective(sum(x[v] for v in g))

    # Dodajanje p.p.
    for va in g:
        for vb in g:
            if va != vb:
                expr = sum(int(bool(g.distance(va, vi) - g.distance(vb, vi))) * x[vi] for vi in g)
                p.add_constraint(expr >= k_value)
            else:
                continue

    # Poskusimo rešiti ILP
    try:
        optimalna_resitev = p.solve()
        vrednosti_za_S = p.get_values(x)
        # Oblikovanje rešitve
        niz_z_rezultatom = f"{k_value} dimension: {optimalna_resitev}"
        # Print tega niza
        # print(niz_z_rezultatom)
        return optimalna_resitev, vrednosti_za_S
    except:
        # If an error occurs (e.g., infeasible), return a special value to indicate infinite dimension
        return float('inf'), None

k = 9
g = graphs.CubeGraph(4)
show(g)

CLP_k_dim(g, k)

