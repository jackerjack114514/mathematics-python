import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x=np.arange(0,25,2)
y=np.array([12,9,9,10,18,24,28,27,25,20,18,15,13])
xnew=np.linspace(0,24,500)
f1=interp1d(x,y,'linear');y1=f1(xnew)
f2=interp1d(x,y,'cubic');y2=f2(xnew)
f3=interp1d(x,y,'nearest');y3=f3(xnew)
f4=interp1d(x,y,'zero');y4=f4(xnew)
f5=interp1d(x,y,'slinear');y5=f5(xnew)
f6=interp1d(x,y,'quadratic');y6=f6(xnew)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')

plt.subplot(2,3,1)
plt.plot(xnew,y1)
plt.xlabel("linear") #分段线性插值

plt.subplot(2,3,2)
plt.plot(xnew,y2)
plt.xlabel("cubic") #三次样条插值

plt.subplot(2,3,3)
plt.plot(xnew,y3)
plt.xlabel("nearest")  #最近邻点插值


plt.subplot(2,3,4)
plt.plot(xnew,y4)
plt.xlabel("zero")

plt.subplot(2,3,5)
plt.plot(xnew,y5)
plt.xlabel("slinear")

plt.subplot(2,3,6)
plt.plot(xnew,y6)
plt.xlabel("quadratic")

plt.savefig('C:\\Users\\Administrator\\Desktop\\figure7_4.png',dpi=500)
plt.show()