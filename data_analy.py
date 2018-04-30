import networkx as nx
f=open("full_data.txt")
h=f.read().split('#')
f.close()
for i in range(len(h)):
    h[i]=h[i].split('\n')
    for j in range(len(h[i])):
        h[i][j]=h[i][j].split(' ')
del h[0]
        
snum={'C':0,'N':0,'O':0,'F':0,'P':0,'S':0,'Cl':0,'Br':0,'Rh':0,'Li':0,'Ga':0,'As':0,'Na':0}
num_list=[]
bnum={}
G=[]
for j in range(len(h)):
    ndict={}
    #num={'C':0,'N':0,'O':0,'F':0,'P':0,'S':0,'Cl':0,'Br':0,'Rh':0,'Li':0,'Ga':0,'As':0,'Na':0}
    node_len=int(h[j][1][0])
    for i in range(2,node_len+2):
        node=h[j][i][0]        
        """        
        try:        
            num[node]+=1
        except:
            num.update({node:1})
        """
        try:
            snum[node]+=1
        except:
            snum.update({node:1})
        ndict.update({i-2:node})
    #num_list.append(num)
    g=nx.Graph()
    g.add_nodes_from(list(range(node_len)))
    for i in range(int(h[j][1][0])+3,int(h[j][int(h[j][1][0])+2][0])+int(h[j][1][0])+3):
        n1=int(h[j][i][0])
        n2=int(h[j][i][1])
        w=h[j][i][2]
        g.add_edge(n1,n2,weight=int(w))
        try:
            bnum[h[j][n1+2][0]+h[j][n2+2][0]+w]+=1
        except:
            bnum.update({h[j][n1+2][0]+h[j][n2+2][0]+w:1})
    nx.set_node_attributes(g,'atom',ndict)
    G.append(g)
#print(snum)
print(bnum)

