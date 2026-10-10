#PageRank值即为 Markov链的平稳分布（转移概率矩阵的转置矩阵其最大特征值对应的归一化特征向量）

import numpy as np,networkx as nx
import pylab as plt
from scipy.sparse.linalg import eigs
L=[(1,2),(2,3),(2,4),(3,4),(3,5),(3,6),(4,1),(5,6),(6,1)]
G=nx.DiGraph()
G.add_nodes_from(range(1,7))
G.add_edges_from(L)
B=np.array(nx.to_numpy_matrix(G))
plt.rc('font',size=16)
pos=nx.shell_layout(G)
nx.draw(G,pos,node_size=280,font_weight='bold',node_color='r',with_labels=True)
plt.savefig('C:\\Users\\Administrator\\Desktop\\fig10_18 Networks.png',dpi=500)
plt.show()  #网络图

A=B/np.tile(B.sum(axis=1,keepdims=True),(1,B.shape[1])) #B.shape[1]: B的行元素个数
A=0.15/B.shape[0]+0.85*A
print("A=\n",A)

print("ans=",B.sum(axis=1,keepdims=True))
W,V=eigs(A.T,1)
V=V.real
V=V.flatten()
V=V/V.sum()
print('V=',V)

plt.figure(2)
plt.bar(range(1,B.shape[0]+1),V,width=0.6,color='b')
plt.savefig('C:\\Users\\Administrator\\Desktop\\fig10_18_2 PageRank.png',dpi=500)
plt.show()