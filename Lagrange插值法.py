#Lagrange插值法

import numpy as np

def h(x,y,a):
    s=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(y)):
            if i!=j:t*=(a-x[j])/(x[i]-x[j])
        s+=t
    return s

x=[1,2,3,4]
y=[1,4,9,16]
a=100

print(h(x,y,a))

#在给定数值对范围内求a值更加精确