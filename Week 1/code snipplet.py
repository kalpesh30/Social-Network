import networkx as nx
import matplotlib.pyplot as pt 


G = nx.DiGraph();
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(2,3),(2,1)])


D = {0:'a',1:'b',2:'c',3:'d'}
for i in D:
    print i
