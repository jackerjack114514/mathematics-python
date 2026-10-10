import sympy as sp
from sympy.abc import t,k,u
from sympy import *

u=symbols("u",cls=Function)
eq=diff(u(t),t)+k*(u(t)-24)
uu=sp.dsolve(eq,ics={u(0):150})
kk=sp.solve(uu,k)  #求解k的表达式
k0=kk[0].subs({t:10.0,u(t):100.0})
print(kk,'\t',k0)
u1=uu.args[1]  #uu:Eq(u(t),24+126*exp(-k*t)), uu.args[0]:u(t), uu.args[1]:24+126*exp(-k*t)
print(u1)
u0=u1.subs({t:20,k:k0})
print(u0)

#另可求数值解
from scipy.integrate import odeint 
import numpy as np
import matplotlib.pyplot as plt

du=lambda u,t:-0.0506*(u-24)
t=np.arange(0,100,0.1)
sol=odeint(du,150,t)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)
plt.plot(t,sol,'r*',label='温度曲线数值解')
plt.plot(t,24+126*np.exp(-0.0506*t),"g+",label='温度函数符号解')
plt.legend()
plt.savefig("C:\\Users\\Administrator\\Desktop\\fig8_7.png",dpi=500)
plt.show()