# getting few details of graphs whose dataset is in graphml, gml and gefx formate

import networkx as nx
import matplotlib.pyplot as plt

#G = nx.read_graphml("/home/kalpesh/Documents/Social Networks/Data_Sets/vecwiki-20091230-manual-coding.graphml")
#print nx.info(G)
# G1 = nx.read_gexf("/home/kalpesh/Documents/Social Networks/Data_Sets/EuroSiS Generale Pays.gexf")

G2 = nx.read_gml('/home/kalpesh/Documents/Social Networks/Data_Sets/karate.gml',label='id')
print nx.info(G2)
