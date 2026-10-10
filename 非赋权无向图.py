#非赋权无向图

import numpy as np
import networkx as nx
import pylab as plt

G=nx.DiGraph()
List=[(1,2),(1,3),(2,3),(3,5),(4,2),(4,6),(5,2),(5,4),(6,5)] #跳过邻接矩阵，直接构造图
G.add_nodes_from(range(1,7))
G.add_edges_from(List)
plt.rc('font',size=16)

pos=nx.kamada_kawai_layout(G)
nx.draw(G,pos,with_labels=True,font_weight='bold',node_color='r')
plt.savefig("非赋权有向图.png",dpi=500)
plt.show()
