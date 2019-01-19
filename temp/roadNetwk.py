# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:59:48 2019

@author: Kalpesh Gupta
"""
import networkx as nx;
import matplotlib as plt;
import random;


city = ['Delhi','Bangalore','Hyderabad','Surat','Ahemdabad','Chennai','Kolkata','Pune']

G = nx.Graph();
for eachCity in city:
    G.add_node(eachCity);

nx.draw(G,label);
plt.show();

cost = [] 
value = 100

while(value < 2000):
    costs.append(value)
    value = value + 100;

print cost