#二次多项式拟合 curve_fit

import numpy as np
from scipy.optimize import curve_fit
y=lambda x,a,b,c:a*x**2+b*x+c #自定义n次多项式拟合

x0=np.arange(0,1.1,0.1)
y0=np.array([-0.447,1.978,3.28,6.16,7.08,7.34,7.66,9.56,9.48,9.30,11.2])

popt,pcov=curve_fit(y,x0,y0)

print("optimize a,b,c:",popt)
print("preview values:",y(np.arange(0.25,0.35,0.01),*popt))
print("preview values:",y(np.array([0.25,0.35]),*popt))
