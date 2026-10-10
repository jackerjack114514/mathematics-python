import numpy as np
import networkx as nx
import pylab as plt

L=[(1,2,5,3),(1,3,3,6),(3,5,4,2),(3,2,1,2),(4,3,1,1),(2,4,2,8),(4,5,3,4),(5,6,5,2),(4,6,2,10)]
G=nx.Graph()
for k in range(len(L)):
    G.add_edge(L[k][0]-1,L[k][1]-1,capacity=L[k][2],weight=L[k][3])

mincostFlow=nx.max_flow_min_cost(G,0,5)
mincost=nx.cost_of_flow(G,mincostFlow)
print("最小费用流：{}\n\n最小费用：{}\n".format(mincostFlow,mincost))

flow_mat=np.zeros((6,6),dtype=int)
for i,adj in mincostFlow.items():
    for j,f in adj.items():
        flow_mat[i,j]=f
print("最小费用最大流的邻接矩阵:\n",flow_mat)

ni,nj=np.nonzero(flow_mat)
n=len(mincostFlow)
key=range(n)   #构造字典序，为顶点标号
s=['v'+str(i+1) for i in range(n)]
s=dict(zip(key,s))

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)
pos=nx.shell_layout(G)

w=nx.get_edge_attributes(G,'capacity')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(ni,nj))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=3)
plt.savefig("C:\\Users\\Administrator\\Desktop\\最小费用最大流.png",dpi=500)
plt.show()
