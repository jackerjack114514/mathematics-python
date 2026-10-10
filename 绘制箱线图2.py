
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

dt=pd.read_excel("C:\\Users\\Administrator\\Desktop\\ppp.xlsx")
a=dt.values
print(a)
h=a[:,::2]
w=a[:,1::2]
h=reshape(h,(-1,1))
w=reshape(w,(-1,1))
hw=np.c_[h,w]

plt.rc("font",size=16)
plt.rc("font",family='SimHei')
plt.boxplot(hw,labels=['身高','体重'])
plt.savefig('fig4_6.png',dpi=500)
plt.show()

#第一四分位数Q1与第三四分位数间距为Q3-Q1=IQR（四分位数间距）
#若存在数据小于Q1-1.5IQR或大于Q3+1.5IQR，则认为它是疑似异常值