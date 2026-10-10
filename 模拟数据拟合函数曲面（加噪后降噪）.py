#模拟数据拟合函数曲面（加噪后降噪）

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from scipy.interpolate import interp2d
from scipy.optimize import curve_fit

m=200;n=300
x=np.linspace(-6,6,m)
y=np.linspace(-8,8,n)

x2,y2=np.meshgrid(x,y)  #(x为行，y为列)

x3=np.reshape(x2,(1,-1))
y3=np.reshape(y2,(1,-1))
xy=np.r_[x3,y3]

def Pfun(t,m1,m2,s):
    return np.exp(-((t[0]-m1)**2+(t[1]-m2)**2)/2*s**2)

z=Pfun(xy,1,2,3)  #e^(-((x-μ1)^2+(y-μ2)^2)/2*σ^2) ,μ1=1,μ2=2,σ=3
zr=z+0.2*np.random.normal(size=z.shape)  #利用随机数加噪

popt,pcov=curve_fit(Pfun,xy,zr)
print("optimized values: μ1={},μ2={},σ={}".format(popt[0],popt[1],popt[2])) #popt为参数拟合结果，pcov为拟合参数的协方差
print("pcov:",pcov)

zn=Pfun(xy,*popt)
zn2=np.reshape(zn,x2.shape)
plt.rc('font',size=16)
plt.rc('font',family='SimHei')

ax=plt.subplot(121,projection='3d')
#ax=plt.axes(projection='3d')
ax.plot_surface(x2,y2,zn2,cmap='gist_rainbow')
ax.set_xlabel("加噪后拟合\nμ1={},μ2={},σ={}".format(popt[0],popt[1],popt[2]))

ax=plt.subplot(122,projection='3d')
z2=np.reshape(zn,x2.shape)
ax.plot_surface(x2,y2,z2,cmap='gist_rainbow')
ax.set_xlabel("原始数据图像")

plt.savefig("fig7_10",dpi=500)
plt.show()

#为何图像不符合二维正态分布形状？
