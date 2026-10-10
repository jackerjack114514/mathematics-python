from scipy.integrate import odeint
import sympy as sp,numpy as np
from numpy import arange

dy=lambda y,x:-2*y+x**2+2*x
x=arange(1,10.5,0.5)

sol=odeint(dy,2,x)
print("x={}\ny={}".format(x,sol.T))