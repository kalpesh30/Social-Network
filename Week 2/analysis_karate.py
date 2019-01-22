# Simple analysis of a simple network

import networkx as nx
import matplotlib.pyplot as plt

#def draw_dege()

G = nx.read_gml('/home/kalpesh/Documents/Social Networks/Data_Sets/karate.gml',label='id')

print nx.is_directed(G)
print set(G.degree())
nx.draw_circular(G)

plt.show()