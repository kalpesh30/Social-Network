# Reading a pajek formate data set and displaying its some basic info

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_pajek("/home/kalpesh/Documents/Social Networks/Data_Sets/football.net")
#G2 = nx.read_pajek("/home/kalpesh/Documents/Social Networks/Data_Sets/patents.net")

print nx.info(G)
print nx.is_directed(G)