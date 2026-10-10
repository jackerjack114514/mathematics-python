#scipy.optimize的fsolve仅给出一个解，而sympy的solve给出了全部解
#fsolve是迭代的数值方法，从一个初始猜测值开始，并沿着一个“局部最优方向”收敛，因此只能找到离初始值最近的解。

from sympy.abc import x,y,z,t
from sympy import solve 
import numpy as np
from sympy import *
from scipy.optimize import fsolve

x1,x2,x3=symbols("x1 x2 x3")

#sympy solve【直接解方程组】
s=solve([5*x2+3,4*x1**2-2*sin(x2*x3),x2*x3-1.5],[x1,x2,x3])
print(s)  

#scipy.optimize【匿名函数】
f=lambda x:[5*x[1]+3,4*x[0]**2-2*sin(x[1]*x[2]),x[1]*x[2]-1.5]
print(fsolve(f,[1.0,1.0,1.0]))

#scipy.optimize【函数定义方程组，避免下标从0开始造成困扰】
def P(x):
    x1,x2,x3=x.tolist()
    return 5*x2+3,4*x1**2-2*sin(x2*x3),x2*x3-1.5

print(fsolve(P,[1.0,1.0,1.0]))