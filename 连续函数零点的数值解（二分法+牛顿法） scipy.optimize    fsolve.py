#x^3+1.1x^2+0.9x-1.4=0
import numpy as np
#from scipy.optimize import fsolve
from scipy import *
from scipy.optimize import *

def binary(f,eps,a,b):
    c=(a+b)/2
    while np.abs(f(c))>eps:
        if f(a)*f(c)<0:b=c
        else:a=c
        c=(a+b)/2
    return c



def newton(f,eps,x0,dx=1E-8):
    def diff(f,dx=dx):
        return lambda x:(f(x+dx)-f(x-dx))/(2*dx)
    df=diff(f,dx)
    x1=x0-f(x0)/df(x0)
    while np.abs(x1-x0)>=eps:
        x1,x0=x1-f(x1)/df(x1),x1
    return x1

f=lambda x:x**3+1.1*x**2+0.9*x-1.4

print(binary(f,1E-6,0,1))
print(newton(f,1E-6,0))
print(fsolve(f,0))