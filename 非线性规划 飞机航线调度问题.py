#非线性规划 飞机航线调度问题

import numpy as np
import pandas as pd
from scipy.optimize import minimize

x0=np.array([150,85,150,145,130,0])
y0=np.array([140,85,155,50,150,0]) #position(xi,yi)

q=np.array([243,236,220.5,159,230,52]) #angles of(vxi,vyi)
d=a0=b0=np.zeros((6,6))
xy0=np.c_[x0,y0]

for i in range(6):
    for j in range(6):
        d[i,j]=np.linalg.norm(xy0[i]-xy0[j])  #norm of Ai and Aj
d[np.where(d==0)]=np.inf #self=inf
a0=np.arcsin(8./d)*180/np.pi #degrees of position line Aij
xy1=x0+1j*y0
xy2=np.exp(1j*q*np.pi/180)
for m in range(6):
    for n in range(6):
        if n!=m: b0[m,n]=np.angle((xy2[n]-xy2[m])/(xy1[m]-xy1[n])) #复数相除取幅角值即为幅角值相减
b0=b0*180/np.pi  #degrees of velocity line vij

print(a0,'\n\n',b0)
#f=pd.ExcelWriter("C:\\Users\\Administrator\\Desktop\\Pan6_1.xlsx")
#pd.DataFrame(a0).to_excel(f,"sheet1",index=None)
#pd.DataFrame(b0).to_excel(f,"sheet2",index=None)

obj=lambda x:np.sum(np.abs(x))
bd=[(-30,30) for i in range(6)]
#x0=np.ones((1,6))
cons=[]
x=[10,20,10,20,10,20]
for i in range(5):
    for j in range(i+1,6):
        #print(i,j,'b0[i,j]:',b0[i,j],'x[i]:',x[i],'x[j]:',x[j],'a0[i,j]:',a0[i,j])
        print(np.abs(b0[i,j]+(x[i]+x[j])/2)-a0[i,j],'\n')
        cons.append({'type':'ineq','fun':lambda x:np.abs(b0[i,j]+(x[i]+x[j])/2)-a0[i,j]})

ans=minimize(obj,np.ones((1,6)),constraints=cons,bounds=bd)  #np.ones((1,6))为初始值
print(ans)

#uncomplicated coding...