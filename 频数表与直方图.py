#频数表与直方图
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
#a=np.loadtxt("C:\\Users\\Administrator\\Desktop\\ppp.xlsx")  #适用于txt

import pandas as pd
dt=pd.read_excel("C:\\Users\\Administrator\\Desktop\\ppp.xlsx",header=None)
a=dt.values

h=a[:,::2];w=a[:,1::2]
#h=np.rehshape(-1,1);w=np.reshape(-1,1)
h=reshape(h,(-1,1))
w=reshape(w,(-1,1))

print(h,w)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')

plt.subplot(121)  #图表1  subplot(1,2,1)与subplot(121)等价，表示生成一行两列的图表，并将当前图置于左侧（依次为参数1、2、1表达意义）
plt.xlabel("身高")
plt.hist(h,10)

plt.subplot(122)  #图表2  subplot(1,2,2)与subplot(122)等价，在上述一行二列的图表中，将当前图置于右侧
ps=plt.hist(w,10)  #plt.hist(w,n) 将w中最小数据至最大数据n等分 
plt.xlabel("体重")

print("体重频数表： ",ps)
plt.savefig('C:\\Users\\Administrator\\Desktop\\fig.png',dpi=500)
plt.show()