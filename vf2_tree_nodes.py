# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:31:21 2016

@author: hunter
"""
import networkx as nx
from read_graph_file import read_graph
from data_analysis import atom_pos

def ematch(G,H,eg,eh):
    return G.node[eg[1]]['atom']==H.node[eh[1]]['atom'] and G[eg[0]][eg[1]]['weight']==H[eh[0]][eh[1]]['weight']

def nmatch(G,H,ng,nh):
    return G.node[ng]['atom']==H.node[nh]['atom']

def next_edge(G,H,ng,eh,match_tree,res_edges,last_node):
    for i in G[ng]:
        #print("Neigh:",eh,(ng,i))
        if i not in match_tree.node and ((ng,i) not in res_edges[eh]):
            #print("Passed:",eh,(ng,i))            
            if ematch(G,H,(ng,i),eh):
                return (ng,i)
    return False

G=read_graph('input.txt')
H=read_graph('dataset.txt')
#G=g[0]
#H=h[1]
#start_G=6
#matched_nodes=atom_pos(G)['C']

#matched_nodes=[25]
#match_tree=nx.DiGraph()
#for i in matched_nodes:
#    match_tree.add_edge('root',i)
def vf2_connected(G,H,start_H,matched_nodes):
    h_dfs=list(nx.dfs_edges(H,start_H))    
    res_edge=dict.fromkeys(h_dfs,[])    
    for start_G in matched_nodes:
        i=0
        g_stack=[]
        #res_edge=[]
        last_node=h_dfs[0][0]
        match_tree=nx.DiGraph()
        match_tree.add_node(start_G)
        h_map={last_node:start_G}
        g_map={start_G:last_node}
        
        #print(stat_G)
        while i<len(h_dfs):
            if last_node!=h_dfs[i][0]:
                start_G=h_map[h_dfs[i][0]]
            current_edge_h=h_dfs[i]
            edge=next_edge(G,H,start_G,current_edge_h,match_tree,res_edge,last_node)
    #           print(match_tree.edges(),"  ",edge," ",h_dfs[i][0]," ",last_node)
           # print("\n",current_edge_h," ",last_node)
            if edge!=False:
                start_G=edge[1]
                g_stack.append(edge)
                
                match_tree.add_edge(edge[0],edge[1])
                last_node=current_edge_h[1]
                h_map.update({last_node:start_G})
                g_map.update({start_G:last_node})
                
                #print("addded: ",edge,current_edge_h)
                i+=1
            #else:
            #    break
            
            else:
    
                i-=1
                if i!=-1:
                    current_edge_h=h_dfs[i]
                    last_edge=g_stack.pop()
                    #print("remov:",last_edge,current_edge_h)
                    
                    #res_edge.append(last_edge)
                    #res_edge[current_edge_h].append(last_edge)
                    res_edge.update({current_edge_h:res_edge[current_edge_h]+[last_edge]})
                    start_G=last_edge[0]
                    last_node=h_dfs[i][0]
                    h_map.pop(g_map[last_edge[1]])
                    g_map.pop(last_edge[1])
                    match_tree.remove_edge(last_edge[0],last_edge[1])
                    match_tree.remove_node(last_edge[1])
                    """
                    for res_i in range(len(res_edge)-1,-1,-1):
                        if res_edge[res_i][0]==last_edge[1]:
                            del res_edge[-1]
                        else:
                            break
                    """
            #print(match_tree.nodes(),"  ",edge)
            #print(h_map)
            #print(g_stack,"  ",edge)
            #print("res:",res_edge)
            if i==-1:
                #print('No Match')
                break
            if i==len(h_dfs):
                #print("Match_Found")
                #print(h_map)
                return h_map
            #print(g_map," ",g_stack)
    return False

def subgraph(g,H):
    start_h=0
    G=list(nx.connected_component_subgraphs(g))
    for i in G:
        atom_loc=atom_pos[i]
        start_atom=H.node[start_h]['atom']
        if start_atom in atom_loc:
            start_g=atom_loc[start_atom]
            if vf2_connected(G,H,start_h,start_g)!=True:
                return True
    return True
    

"""
atom='O'            
nn=[]
for i in range(len(H)):
    j=atom_pos(H[i])
    if atom in j:
        nn.append((i,j[atom][0]))
n=[]
for i in range(len(G)):
    j=atom_pos(G[i])
    if atom in j:
        n.append((i,j[atom]))

for i in n:
    for j in nn:
        if vf2_connected(G[i[0]],H[j[0]],j[1],i[1])!=False:
            print(i[0],"  ",j[0])        
   
9,12
{0: 5, 1: 11, 2: 12, 3: 10, 4: 4, 5: 9, 6: 3, 7: 0, 8: 13, 9: 6, 10: 2}


1    62
2    75
3    63
6    65
8    0
9    4
9    11
9    41
9    97
9    98
0    16
0    22
0    60
2    75
5    16
5    19
5    22
5    37
5    40
5    60
5    73
6    2
7    19
7    22
7    35
7    37
7    40
7    45
7    60
7    64
7    85
9    4
9    41
9    70

"""


