import numpy as np
import networkx as nx
import pylab as plt

List=[(1,2,9),(1,3,2),(1,4,4),(1,5,7),(2,3,3),(2,4,4),(3,4,8),(3,5,4),(4,5,6)]
#print(np.size(i),np.size(j),np.size(w))  #9 9 9
G=nx.Graph()
G.add_nodes_from(range(1,6))
G.add_weighted_edges_from(List)  #取edges中的加权边
w=nx.get_edge_attributes(G,'weight')

plt.rc('font',size=16)
plt.rc('font',family="SimHei")
plt.rc("axes",unicode_minus=False)
plt.figure(figsize=(12,12)) 

plt.subplot(121)
nx.draw(G,font_weight='bold') 

plt.subplot(122)
pos=nx.circular_layout(G) #布局设置，将节点按照“同心圆壳（shells）”的结构排布，适合展示分层结构或分组结构
w=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G,pos,with_labels=True,font_weight='bold',font_size=12)
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
plt.xlabel("circular_layout")

plt.savefig("C:\\Users\\Administrator\\Desktop\\fig10_2_2.png",dpi=500)
plt.show()


"""
Graph()
Graph(A)
DiGraph()
DiGraph(A)
MultiGraph()
MultiDiGraph()
add_edge()
add_edges_from(List)
add_node()
add_nodes_from(List)
dijkstra_path(G,source,target,weight='weight')
dijkstra_path_length(G,source,target,weight='weight')


布局函数	图形结构	特点 / 适用场景
spring_layout	力导向（自由分布）	最常用、自动美观、适合一般图
kamada_kawai_layout	力导向（更规则）	距离优化，美观且规则
circular_layout	单圆结构	所有节点围成一圈
shell_layout	多层同心圆	节点分层或分组展示
random_layout	随机散点	基本无序，只用于测试
spectral_layout	线性/矩形结构	基于矩阵特征向量，适合谱聚类可视化
planar_layout	平面图布局	仅适用于平面图（无交叉边）
spiral_layout	螺旋结构	节点沿螺旋排布
bipartite_layout	左右两层结构	二部图（上下或左右两排）
multipartite_layout	多部图结构	多个竖直分层结构
"""