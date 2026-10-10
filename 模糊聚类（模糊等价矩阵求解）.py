from numpy import array,zeros,triu
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
  #cluster:类别 hierarchy:分层
def hc(a,b):
    m,N=a.shape  #a:mxN, b:Nxn
    n=b.shape[1]
    c=zeros((m,n))
    for i in range(m):
        for j in range(n):
            c[i,j]=max([min(a[i,k],b[k,j]) for k in range(N)])
    return c

a=array([[5,5,3,2],[2,3,4,5],[5,5,2,3],[1,5,4,1],[2,4,5,1]])
d=array([[sum(abs(a[i]-a[j])) for i in range(5)] for j in range(5)])  #曼哈顿距离
print(a,'\n',d,'\n')

r=1-0.1*d
print("由曼哈顿距离求得相似系数：",r)

tr=hc(r,r)
while abs(r-tr).sum()>0.00001:r=tr,tr=hc(r,r)  #二次法求传递闭包矩阵（模糊等价矩阵）
print('\n\n')

d2=1-tr
d2=triu(d2,1)
d2=d2[d2!=0]  #提取矩阵上三角中的非零元素

z=sch.linkage(d2)
s=['Ⅰ','Ⅱ','Ⅲ','Ⅳ','Ⅴ']
sch.dendrogram(z,labels=s) #聚类树
plt.yticks()  #隐藏y轴
plt.savefig('C:\\Users\\Administrator\\Desktop\\fig14_9.png',dpi=500)
plt.show()

#未完成编译