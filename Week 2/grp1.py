import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy

def add_nodes(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

def add_random_edge(G):
    while(True):
        v1 = random.choice(list(G.nodes()))
        v2 = random.choice(list(G.nodes()))
        if  v1 != v2 :
            G.add_edge(v1,v2)
            break
    return G

def make_connected(G):
    while(nx.is_connected(G) == False):
        G = add_random_edge(G)
    return G

def edges_for_connectedness(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G = make_connected(G)
    return G.number_of_edges()

def get_avg_no_of_edges_for_connectedness(n):
    sm = 0
    for i in range(10):
        sm = sm + edges_for_connectedness(n)
    return sm/4

def plotting_connected_edges_no():
    x = []
    y = []
    i = 10
    while (i<400):
        x.append(i)
        y.append(get_avg_no_of_edges_for_connectedness(i))
        i = i+10
    plt.plot(x,y)
    plt.xlabel("No. of nodes")
    plt.ylabel("No. of edges required for connectedness")
    plt.show()