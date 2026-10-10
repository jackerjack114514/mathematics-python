#Logistic模型预测人口增长

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

a=np.arange(1790,2010,10)
b=np.array([3.9,5.3,7.2,9.6,12.9,17.1,23.2,31.4,38.6,50.2,62.9,76.0,92.0,106.5,123.2,131.7,150.7,179.3,204.0,226.5,251.4,281.4])

c=np.r_[a,b]
x=lambda t,r,xm:xm/(1+(xm/3.9-1)*np.exp(-r*(t-1790))) 
bd=((0,200),(0.1,1000))
popt,pcov=curve_fit(x,a[1:],b[1:],bounds=bd)
print(popt)
print(x(2010,*popt))

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)

plt.plot(a,b,'r-',label='fact')
plt.legend()
plt.show()