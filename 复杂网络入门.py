import numpy as np
import networkx as nx
L=[(1,2),(1,3),(2,3),(2,4),(2,5),(3,5),(4,5),(4,6)]
G=nx.Graph()
G.add_nodes_from(range(1,7))
G.add_edges_from(L)

D=nx.diameter(G) #网络直径
LH=nx.average_shortest_path_length(G) #平均路径长度

Ci=nx.clustering(G) #各顶点的聚类系数
C=nx.average_clustering(G) #网络的平均聚类系数

print("网络直径:{}\n平均网络长度:{}\n".format(D,LH))

print("各顶点聚类系数:")
for index,value in enumerate(Ci.values()):
    print('(顶点v{:d}:{:.4f});'.format(index+1,value),end=' ')
print("\n网络聚类系数:{:.4f}".format(C))


