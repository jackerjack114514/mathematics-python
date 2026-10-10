from scipy.integrate import odeint
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def lorenz(w,t):
    s=10
    r=28
    b=8/3
    x,y,z=w
    return np.array([s*(y-x),r*x-y-x*z,x*y-b*z])

t=np.arange(0,50,0.01)
sol1=odeint(lorenz,[0.0,1.0,0.0],t)  #给出变量范围（时间段）内的数值解，返回三列的矩阵，第i列对应第i个函数的数值解
sol2=odeint(lorenz,[0.0,1.0001,0.0],t)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False) 

plt.figure(figsize=(12, 12)) 
#point！ figsize=(12,12) 表示12x12英寸，即1200x1200像素（1英寸=100像素）

ax1=plt.subplot(131,projection='3d')
ax1.set_xlabel("x");ax1.set_ylabel("y");ax1.set_zlabel("z")
ax1.plot(sol1[:,0],sol1[:,1],sol1[:,2],'r')

ax2=plt.subplot(132,projection='3d')
ax2.plot(sol1[:,0]-sol2[:,0],sol1[:,1]-sol2[:,1],sol1[:,2]-sol2[:,2],'g')
ax2.set_xlabel("x");ax2.set_ylabel("y");ax2.set_zlabel("z")

ax3=plt.subplot(133,projection='3d')
ax3.set_xlabel("x");ax3.set_ylabel("y");ax3.set_zlabel("z")
ax3.plot(sol2[:,0],sol2[:,1],sol2[:,2],"g")

plt.savefig('C:\\Users\\Administrator\\Desktop\\fig8_6.png',dpi=500)
plt.show()

print("sol1={}\nsol1-sol2={}".format(sol1,sol1-sol2))
