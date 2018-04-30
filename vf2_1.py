import networkx as nx
a=nx.Graph()
a.add_weighted_edges_from([(1,2,1),(2,3,1),(2,4,2),(3,4,1),(3,5,1)])
b=nx.Graph()
b.add_weighted_edges_from([(1,2,1),(2,3,1),(1,3,1),(3,4,2)])
c=nx.Graph()
c.add_weighted_edges_from([(1,2,2),(2,3,1),(1,3,1),(3,4,1)])
nx.set_node_attributes(a,'atom',{1:'N',2:'C',3:'C',4:'C',5:'O'})
nx.set_node_attributes(b,'atom',{1:'C',2:'C',3:'C',4:'O'})
nx.set_node_attributes(c,'atom',{1:'C',2:'C',3:'C',4:'N'})

def ematch(G,H,eg,eh):
    return G.node[eg[2]]['atom']==H.node[eh[2]]['atom'] and G[eg[1]][eg[2]]['weight']==H[eh[1]][eh[2]]['weight']
def nmatch(G,H,ng,nh):
    return G.node[ng]['atom']==H.node[nh]['atom']

def n_uvisit_init(G):
    return dict.fromkeys(G.edges_iter(),False)
def e_uvisit_init(G):
    return set(G.nodes_iter())

a_n_uvisited=n_uvisit_init(a)
b_n_uvisited=n_uvisit_init(b)
b_dfs=nx.edge_dfs(b,4)
a_e_uvisited=e_uvisit_init(a)
a_stack=[]
current_b=4

def next_edge(G,H,ng,eh,a_e_uvisited):
    for i in G[ng]:
        if (ng,i) in a_e_uvisited or (ng,i) in a_e_uvisited:
            if ematch(G,H,(ng,i),eh):
                return (ng,i)
    return False


            