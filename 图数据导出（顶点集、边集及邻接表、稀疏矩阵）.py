import numpy as np
import networkx as nx
import pylab as plt

a=np.loadtxt("Pdata10_2.txt")
G=nx.Graph(a)
print("图的顶点集:{}\n\n图的边集:{}".format(G.nodes(),G.edges()))
print("图的邻接表:",list(G.adjacency()))
print("图的列表字典:",nx.to_dict_of_dicts(G))
B=nx.to_numpy_matrix(G)  #导出图G的邻接矩阵B
C=nx.to_scipy_sparse_matrix(G)  #导出图G的稀疏矩阵C

print(B,C)


      
