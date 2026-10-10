#流行病动力学 Kermack-Mckendrick方程 (传染病不致死的情形)

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s,i,r
from sympy import *

f=0.01 #传染性接触率，取决于卫生水平
m=0.05  #恢复系数，取决于医疗水平
n=300  #封闭环境内的总人数，满足s+i+r=n
s0=100 #初始易感人群
i0=10  #初始感染人群
r0=190  #初始免疫人群
#以上为传染模型的参数

def KM(w,t):
    s,i,r=w
    return np.array([-f*s*i,f*s*i-m*i,m*i])
#无需加入条件：s+i+r=n

t=np.arange(0,100,0.01)
sol=odeint(KM,[s0,i0,r0],t)

print(sol)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)

#plt.figure(figsize=(12,12))
plt.plot(t,sol[:,0],"b*",label="易感人数,初始有{}人".format(s0))
plt.plot(t,sol[:,1],"r*",label="感染人数,初始有{}人".format(i0))               
plt.plot(t,sol[:,2],"g*",label="免疫人数,初始有{}人".format(r0))
plt.xlabel("传染性接触率为{}  恢复系数为{}".format(f,m))
plt.legend()
plt.savefig('C:\\Users\\Administrator\\Desktop\\流行病KM模型.png',dpi=500)
plt.show()
