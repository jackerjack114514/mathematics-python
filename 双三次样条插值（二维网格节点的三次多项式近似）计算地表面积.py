#双三次样条插值（二维网格节点的三次多项式近似）
#对应地把所计算的三维曲面剖分成个小曲面进行计算，每个小曲面的面积用对应的三维空间中4个点所构成的两个小三角形面积的和作为近似值。

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from scipy.interpolate import interp2d 
import pandas as pd

dt=pd.read_excel("C:\\Users\\Administrator\\Desktop\\高程数据表.xlsx",header=None)
z=dt.values
x=np.arange(0,1000,100)
y=np.arange(0,1000,100)
f=interp2d(x,y,z,'cubic')   #POINT
xn=np.linspace(0,1000,101)
yn=np.linspace(0,1000,101)  
zn=f(xn,yn)

m=len(xn);n=len(yn)
s=0

for i in np.arange(m-1):
    for j in np.arange(n-1):
        p1=np.array([xn[i],yn[j],zn[j,i]]) #zn[j,i]? zn[i,j]?
        p2=np.array([xn[i+1],yn[j],zn[j,i+1]])
        p3=np.array([xn[i+1],yn[j+1],zn[j+1,i+1]])
        p4=np.array([xn[i],yn[j+1],zn[j+1,i]])

        p12=norm(p1-p2)
        p23=norm(p3-p2)
        p13=norm(p3-p1)
        p14=norm(p4-p1)
        p34=norm(p4-p3)

        L1=(p12+p23+p13)/2
        L2=(p13+p14+p34)/2

        s1=np.sqrt(L1*(L1-p12)*(L1-p23)*(L1-p13))
        s2=np.sqrt(L2*(L1-p13)*(L2-p14)*(L2-p34))
        s=s+s1+s2
print("s=",s)

plt.rc('font',size=16)
#plt.rc('text',usetex=True) 
plt.subplot(121)
contr=plt.contour(xn,yn,zn)  #等高线图
plt.clabel(contr)
plt.xlabel("x")
plt.ylabel("y")

ax=plt.subplot(122,projection='3d')
X,Y=np.meshgrid(xn,yn)
ax.plot_surface(X,Y,zn,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig('fig.png',dpi=500)
plt.show()
