# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:59:48 2019

@author: Kalpesh Gupta
"""
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy.random


city = ['Delhi','Bangalore','Hyderabad','Surat','Ahemdabad','Chennai','Kolkata','Pune']

G = nx.Graph();
for eachCity in city:
    G.add_node(eachCity)

nx.draw(G)
plt.show()


cost = [] 
value = 100

while(value < 2000):
    cost.append(value)
    value = value + 100

print cost
try:
    while (G.number_of_edges() < 16):
        c1 = random.choice(list(G.nodes()))
        c2 = random.choice(list(G.nodes()))
        if c1!=c2 and G.has_edge(c1,c2) == 0:
            w = random.choice(cost)
            G.add_edge(c1,c2,weight=w)
except IndexError as error:
    print "error"

pos = nx.spectral_layout(G)
nx.draw(G,pos)
plt.show()
