#匹配问题(赋权二分图的最大完美对集)

import numpy as np
import networkx as nx
from networkx.algorithms.matching import *
#from networkx.algorithms.matching import max_weight_matching

a=np.array([[3,5,5,4,1],[2,2,0,2,2],[2,4,4,1,0],[0,2,2,1,0],[1,2,1,3,3]])
b=np.zeros((10,10))
b[0:5,5:]=a
G=nx.Graph(b)
s0=max_weight_matching(G)  #point
s=[sorted(w) for w in s0]
#print(s)
L1=[x[0] for x in s];L1=np.array(L1)+1
L2=[x[1] for x in s];L2=np.array(L2)-4
c=a[L1-1,L2-1]
d=c.sum()
print("分配人员编号：{}\n工作编号：{}\n工作对应安排：{}\n总效益：{}".format(L1,L2,list(zip(L1,L2)),d))

