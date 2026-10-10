import numpy as np
import pylab as plt
import networkx as nx
import pandas as pd

a=pd.read_excel("C:\\Users\\Administrator\\Desktop\\Pdata10_14.xlsx",header=None)
b=a.values
b[np.isnan(b)]=0 #空白格赋初始值0（不用inf，networkx模块默认无边连接处距离为0）
c=np.zeros((8,8))
c[0:7,1:8]=b #规范格式
G=nx.Graph(c)
T=nx.minimum_spanning_tree(G)
d=nx.to_numpy_matrix(T) #最小生成树的邻接矩阵
print("minimum_spanning_tree:",d)
W=d.sum()/2+5 #对称矩阵，距离计算了两遍
print("total length of the tube:",W)

s=dict(zip(range(8),range(1,9)))
plt.rc('font',size=16)
pos=nx.shell_layout(G)  
nx.draw(G,pos,with_labels=False)  #with_labels=True 时，顶点标号会重叠而不是覆盖

wid=np.array([1,2,3,4,5,6,7])
nx.draw(T,pos,node_size=280,node_color='r',edge_color="#00ff00", edge_cmap=plt.cm.Blues,labels=s,width=wid,) #edge_color="#00ff00", edge_cmap=plt.cm.Blues 必须一同出现！

"""
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    edge_color=edge_colors,   # 根据权重着色
    edge_cmap=plt.cm.Blues,   # 颜色映射
    width=edge_widths,        # 边宽度
    font_size=12
)
"""

w=nx.get_edge_attributes(T,'weight')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.savefig("C:\\Users\\Administrator\\Desktop\\fig10_14.png",dpi=500)
plt.show()

