#dijkstra 最短路径算法

import numpy as np
import math
inf=math.inf

def Dijkstra_minpath(matr,start): #matr:图G的邻接矩阵数组
    n=len(matr) #总节点数
    dis=[];temp=[]  #dis:l(v), temp:
    dis.extend(matr[start])  #与初始节点关联的顶点
    temp.extend(matr[start])
    temp[start]=inf
    visited=[start] #永久标号
    parent=[start]*n  #使得成为最短路径的父节点，初始化默认为起点（degree=1）
    
    while len(visited)<n:  #求两点间最短路径时可以不用遍历visited=n,终点进入visited（永久节点）时即可终止
        i=temp.index(min(temp)) #最小节点坐标
        temp[i]=inf #使i加入永久标号，踢出临时标号
        for j in range(n):
            if j not in visited:
                if(dis[i]+matr[i][j])<dis[j]: #此前加入visited的节点在其循环中已经比对过，故不再讨论
                    dis[j]=temp[j]=dis[i]+matr[i][j]
                    parent[j]=i
        visited.append(i) #已处理节点i
        path=[]
        path.append(str(i))
        k=i
        while(parent[k]!=start):
            path.append(str(parent[k]))
            k=parent[k] #从终点出发，依次溯源父节点
        path.append(str(start))
        path.reverse() 
        print(str(i)+':','->'.join(path)) #每次循环处理一个节点i，输出起点到vi的最短路径
    return dis

a=[[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],[2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],[7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],[4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]]
d=Dijkstra_minpath(a,3) #顶点v3到所有顶点的最短距离

ans=zip(range(9),d)
print("minpath for v3 to other vertexs:",list(ans))
