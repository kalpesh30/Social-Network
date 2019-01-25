# Simple analysis of a simple network

import networkx as nx
import matplotlib.pyplot as plt


def draw_dege(G):
    D = list(G.degree())
    all_degree = []
    for i in range(len(D)):
        all_degree.append(D[i][1])
    ndeg = list(set(all_degree))
    count_of_degrees = []
    for i in ndeg:
        x = all_degree.count(i)
        count_of_degrees.append(x)

    plt.plot(ndeg,count_of_degrees)
    plt.show();  




G = nx.read_gml('/home/kalpesh/Documents/Social Networks/Data_Sets/karate.gml',label='id')

print nx.is_directed(G)

nx.draw_circular(G)
plt.show()

draw_dege(G)

print nx.density(G)  # density of network

print nx.clustering(G)  # clustering coefficient dict
s = 0
for i in nx.clustering(G).values():
    s = s + i
    print i
print "clustering " + str(s/len(nx.clustering(G)))  # average clustering
#G.average_clustering(G)
