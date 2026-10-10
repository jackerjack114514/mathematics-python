#一次线性微分方程组的数值解与符号解

from scipy.integrate import odeint
from sympy.abc import T
import numpy as np
import matplotlib.pyplot as plt

def Pfun(y,x):
    y1,y2=y
    return y2,-2*y1-2*y2 #return np.array([y2,-2*y1-2*y2]) 等价

x=np.arange(0,10.1,0.1)

sol1=odeint(Pfun,[0.0,1.0],x)
plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)

plt.plot(x,sol1[:,0],"r*",label='数值解散点')
plt.plot(x,np.exp(-x)*np.sin(x),'g',label="符号解曲线")
plt.legend()  #显示绘图的labels
plt.savefig("C:\\Users\\Administrator\\Desktop\\fig8_5.png",dpi=500)
plt.show()