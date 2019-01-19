# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 2019

@author: Kalpesh Gupta
"""

import networkx as nx
import matplotlib.pyplot as plt
#import random

G = nx.read_edgelist("/home/kalpesh/Documents/Social Networks/Data_Sets/facebook_combined.txt")
print nx.info(G)

print nx.number_of_edges(G)
print nx.number_of_nodes(G)
print nx.is_directed(G)