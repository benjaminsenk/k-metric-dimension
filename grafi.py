#hiperkocka
C = graphs.CubeGraph(4)
C.show()

#pot
p1 = graphs.PathGraph(4)
p1.show()

p2 = graphs.PathGraph(5)
p2.show()

#kartezični produkt poti
P = p1.cartesian_product(p2)
P.show()
p3 = graphs.PathGraph(3)
P1 = P.cartesian_product(p3)
P1.show()

#kartezični produkt ciklov
c1 =graphs.CycleGraph(5)
c1.show()

c2 =graphs.CycleGraph(4)
c2.show()

C = c1.cartesian_product(c2)
C.show()


#drevesa
T = graphs.BalancedTree(4,2)
T.show()

from sage.graphs.graph_plot import GraphPlot
G = graphs.HoffmanSingletonGraph()
T = Graph()
T.add_edges(G.min_spanning_tree(starting_vertex=0))
T.show(layout='tree', tree_root=0)

T = list(graphs.trees(7))
t = T[2]
t.show()

T = list(graphs.trees(7))
t = T[3]
t.show()


len(T)

#poljuben graf z matriko sosedov
g = Graph({
    '0': ['1', '3'],
    '1': ['0', '3'],
    '2': ['3'],
    '3': ['0', '2']
})








