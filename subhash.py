import networkx as nx
a=nx.Graph()
a.add_weighted_edges_from([(1,2,1),(2,3,1),(2,4,1),(3,4,1),(3,5,1)])
b=nx.Graph()
b.add_weighted_edges_from([(1,2,1),(2,3,1),(1,3,1),(3,4,2)])
c=nx.Graph()
c.add_weighted_edges_from([(1,2,1),(2,3,1),(1,3,1)])
nx.set_node_attributes(a,'atom',{1:'N',2:'C',3:'C',4:'C',5:'O'})
nx.set_node_attributes(b,'atom',{1:'C',2:'C',3:'C',4:'O'})
nx.set_node_attributes(c,'atom',{1:'C',2:'C',3:'C'})

def ematch(G,H,eg,eh):
    return G.node[eg[1]]['atom']==H.node[eh[1]]['atom'] and G[eg[0]][eg[1]]['weight']==H[eh[0]][eh[1]]['weight']
def nmatch(G,H,ng,nh):
    return G.node[ng]['atom']==H.node[nh]['atom']

def n_uvisit_init(G):
    return dict.fromkeys(G.nodes_iter(),False)
def e_uvisit_init(G):
    return set(G.edges_iter())

a_n_uvisited=n_uvisit_init(a)
b_n_uvisited=n_uvisit_init(c)

b_dfs=list(nx.edge_dfs(c,1))
a_e_uvisited=e_uvisit_init(c)
a_stack=[]
current_b=4

def next_edge(G,H,ng,eh,a_e_uvisited,g_map,h_map):
    for i in G[ng]:
        if (ng,i) in a_e_uvisited or (i,ng) in a_e_uvisited:
            if ematch(G,H,(ng,i),eh):
                if h_map[eh[1]]==0:
                    h_map.update({eh[1]:1})
                    g_map[i]=eh[1]                    
                    return (ng,i)
                elif i not in g_map:
                    False
                elif g_map[i]==eh[1]:
                    #print('there')
                    h_map[eh[1]]+=1 
                    return (ng,i)
    return False

from read_graph_file import read_graph

G=nx.Graph()
G.add_weighted_edges_from([(1,3,1),(1,4,1),(4,5,1),(2,4,1),(3,4,1),(2,5,1)])
H=nx.Graph()
H.add_weighted_edges_from([(1,2,1),(2,3,1),(1,3,1)])
nx.set_node_attributes(G,'atom',{1:'O',2:'O',3:'N',4:'N',5:'C'})
nx.set_node_attributes(H,'atom',{1:'O',2:'N',3:'C'})

G=read_graph('input.txt')
H=read_graph('dataset.txt')
#G=read_graph('input.txt')[0]
#H=read_graph('dataset.txt')[0]
def connected_subgraph(G,H,start_node,matched_nodes):
    h_dfs=list(nx.edge_dfs(H,start_node))
    for start in matched_nodes:
        h_map=dict.fromkeys(H.nodes(),0)
        h_map[h_dfs[0][0]]=1
        g_map={start:h_dfs[0][0]}
        g_un=set(G.edges())
        i=0
        g_stack=[]
        last_node=h_dfs[0][0]
        while i<len(h_dfs):
            if last_node!=h_dfs[i][0]:
                for node in g_map:
                    if g_map[node]==h_dfs[i][0]:
                        start=node
            edge=next_edge(G,H,start,h_dfs[i],g_un,g_map,h_map)
            if edge!=False:
                try:
                    g_un.remove(edge)
                except:
                    g_un.remove((edge[1],edge[0]))
                start=edge[1]
                g_stack.append(edge)
                #print(edge)
                i+=1
            
            else:
                i-=1
                if i!=-1:
                    last_edge=g_stack.pop()
                    start=last_edge[0]
                    h_map[g_map[last_edge[0]]]-=1
                    res_edge=[]
                    for res_i in range(len(g_stack)-1,-1,-1):
                        if g_stack[res_i][0]==start:
                            res_edge.append(g_stack.pop())
                    g_un.update(res_edge)
                    for res in res_edge:
                        h_map[g_map[res[0]]]-=1
                        
            if i==-1:
                #print('No Match')
                break
            if i==len(h_dfs):
                #print("Match_Found")
                #print(g_stack)
                #print(g_map)
                return g_map
            #print(g_map," ",g_stack)
    return False
    
        


            