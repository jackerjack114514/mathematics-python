#超定线性方程组的最小二乘解（线性拟合经验函数）
import numpy as np
import numpy.linalg as LA
from matplotlib.pyplot import *
x=np.array([0,1,2,3])
y=np.array([-1,0.2,0.9,2.1])
A=np.c_[x,np.ones_like(x)]   #np.ones_like():Return an array of ones with the same shape and type as a given array.
m,c=LA.lstsq(A,y,rcond=None)[0]
print(m,c);rc('font',size=16)
plot(x,y,'o',label='original data',markersize=5)
plot(x,m*x+c,'r',label='optimize line')
rc('font',family='SimHei')   #用于显示中文标签
rc('axes',unicode_minus=False)  #用于正常显示符号
legend();
savefig('figure.png',dpi=500)
show()
