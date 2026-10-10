#dijkstra模块调用

import numpy as np
import networkx as nx
List=[(0,1,1),(0,2,2),(0,4,7),(0,6,4),(0,7,8),(1,2,2),(1,3,3),(1,7,7),(2,3,1),(2,4,5),(3,4,3),(3,5,6),(4,5,4),(4,6,3),(5,6,6),(5,7,4),(6,7,2)]
G=nx.Graph()
G.add_weighted_edges_from(List)
A=nx.to_numpy_matrix(G,nodelist=range(8))
np.savetxt('C:\\Users\\Administrator\\Desktop\\Pdata10_6.txt',A)
p=nx.dijkstra_path(G,source=3,target=7,weight='weight')  #输出最短路径
d=nx.dijkstra_path_length(G,3,7,weight='weight')  #输出最短距离
print("minpath:{}\nminlength:{}".format(p,d))

#networkx中，无边连接的两个顶点间对应的邻接矩阵元素为0，而非＋∞
