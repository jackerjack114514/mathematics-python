#最小生成树 kruskal/prim/boruvka
import numpy as np
import networkx as nx
import pylab as plt
L=[(1,2,8),(1,3,4),(1,5,2),(2,3,4),(3,4,2),(3,5,1),(4,5,5)]
G=nx.Graph()
G.add_nodes_from(range(1,6))
G.add_weighted_edges_from(L)

T=nx.minimum_spanning_tree(G) #最小生成树模块
#T=minimum_spanning_tree(G, weight='weight', algorithm='kruskal')  algorithm可取：'kruskal'，'prim'，或'boruvka'，缺省值（默认值）为'kruskal'；

w=nx.get_edge_attributes(T,'weight')
TL=sum(w.values())
print("minimum_spanning_tree:{}\n\ntotal length of minimum_spanning_tree:{}".format(w,TL))

print("T:",T)
pos=nx.shell_layout(G)
nx.draw(T,pos,node_size=280,with_labels=True,node_color='r')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.savefig("C:\\Users\\Administrator\\Desktop\\fig10_3_1.png",dpi=500)
plt.show()