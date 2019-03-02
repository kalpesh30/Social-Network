import networkx as nx
import matplotlib.pyplot as plt
import math
import random

def create_graph():
    G = nx.Graph()
    # Adding nodes to the graph
    for i in range(1,101):
        G.add_node(i)
    return G

def getsize(G):
    size = []
    for each in G.nodes():
        if(G.node[each]['type'] == 'person'):
            size.append(G.node[each]['name'] * 10)
        else:
            size.append(800)
    return size

def visualise(G,labeldict,sizearray,colorarray):
    nx.draw(G,labels = labeldict,node_size=sizearray,node_color = colorarray)
    plt.show()

def assign_bmi(G):
    for each in G.nodes():
        G.node[each]['name'] = random.randint(15,40)
        G.node[each]['type'] = 'person'

def getLabels(G):
    dict1 = {}
    for each in G.nodes():
        dict1[each] = G.nodes[each]['name']
    return dict1

def add_foci_nodes(G):
    n = G.number_of_nodes()
    i = n + 1
    foci_nodes = ['gym','karate','eatout','movie_club','yoga_club']
    for j in range(5):
        G.add_node(i)
        G.node[i]['type'] = 'foci'
        G.node[i]['name'] = foci_nodes[j] 
        i = i + 1  

def get_colors(G):
    c = []
    for each in G.nodes():
        if G.node[each]['type'] == 'person':
            c.append('blue')
        else:
            c.append('yellow')
    return c

def get_foci_nodes(G):
    foci_nodes = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'foci':
            foci_nodes.append(each)
    return foci_nodes

def get_person_nodes(G):
    person_nodes = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'person':
            person_nodes.append(each)
    return person_nodes

def add_foci_edges(G):
    foci_nodes = get_foci_nodes(G)
    person_nodes = get_person_nodes(G)
    for each in person_nodes:
       r = random.choice(foci_nodes)
       G.add_edge(each,r)


G = create_graph()
assign_bmi(G)
add_foci_nodes(G)
labeldict = getLabels(G)
colors = get_colors(G)
add_foci_edges(G)
visualise(G,labeldict,getsize(G),colors)

