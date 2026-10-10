import numpy as np,sympy as sp
from matplotlib.pyplot import *
import numpy.linalg as LA

x=np.array(range(0,8))
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8])
A=np.c_[x,np.ones_like(x)]
m,c=LA.lstsq(A,y,rcond=None)[0]
print("y={}x+{}".format(m,c))   #numpy 与 sympy 冲突，无法进行m.n(5)等操作
plot(x,y,'o',label='original data',markersize=5)
plot(x,m*x+c,'r',label='optimized line')
rc('font',family='SimHei')
rc('axes',unicode_minus=False)
legend()
savefig('fig.png',dpi=500)
show()

#或利用超定线性方程的最小二乘解，也可进行线性拟合
from numpy.linalg import pinv
A=np.array([[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]])
B=y.reshape(8,1)
ans=pinv(A).dot(B)
print("y={}x+{}".format(ans[0],ans[1]))

