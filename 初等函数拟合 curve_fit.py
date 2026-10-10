#初等函数拟合 curve_fit

import numpy as np
from scipy.optimize import curve_fit
x0=np.array([6,2,6,7,4,2,5,9])
y0=np.array([4,9,5,3,8,5,8,2])
z0=np.array([5,2,1,9,7,4,3,3])

xy0=np.r_[x0,y0]  #xy9=np.vstack([x0,y0])

def Pfun(t,a,b,c):
    return a*np.exp(b*t[0])+c*t[1]**2
#popt,pcov=curve_fit(Pfun,xy0,z0)

P=lambda x,a,b,c:a*np.exp(b*x[0])+c*x[1]**2  #效果相同，语法也几乎相同
popt,pcov=curve_fit(P,xy0,z0)
print("optimized values of a,b,c:",popt)

#bugs here: true answer is a=5.0891,b=-0.0026,c=-0.0215 ,but funtion returns a=9.3461,b=-1.1399,c=1.060

