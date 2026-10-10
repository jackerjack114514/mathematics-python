#函数的k阶差分
import numpy as np
from numpy import sin,cos

def diff_forward(f,k,h,x): #k阶差分，h为步长，x为初始值
    if k<=0:return f(x)
    else: return diff_forward(f,k-1,h,x+h)-diff_forward(f,k-1,h,x)

f=lambda x:np.sin(x)
k=3;h=0.01;x=0
print('步长为{}时，在x={}处的的{}阶差分值：{}'.format(h,x,k,diff_forward(f,k,h,x)))
print('在x={}处的{}阶导数值:{}'.format(x,k,diff_forward(f,k,0.001,x)/(0.001)**k))

