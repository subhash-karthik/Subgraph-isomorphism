# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:12:07 2016

@author: hunter
"""

import networkx as nx
def read_graph(filename):
    f=open(filename)
    h=f.read().split('#')
    f.close()
    for i in range(len(h)):
        h[i]=h[i].split('\n')
        for j in range(len(h[i])):
            h[i][j]=h[i][j].split(' ')
    del h[0]
            
    G=[]
    for j in range(len(h)):
        ndict={}
        node_len=int(h[j][1][0])
        for i in range(2,node_len+2):
            node=h[j][i][0]        
            ndict.update({i-2:node})
        
        g=nx.Graph()
        g.add_nodes_from(list(range(node_len)))
        for i in range(int(h[j][1][0])+3,int(h[j][int(h[j][1][0])+2][0])+int(h[j][1][0])+3):
            n1=int(h[j][i][0])
            n2=int(h[j][i][1])
            w=h[j][i][2]
            g.add_edge(n1,n2,weight=int(w))
        nx.set_node_attributes(g,'atom',ndict)
        G.append(g)
    return G


