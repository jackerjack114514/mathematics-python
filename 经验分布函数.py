#经验分布函数（n趋于∞时，由离散数据得出的经验分布函数将收敛于分布函数）

import numpy as np
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

dt=pd.read_excel("C:\\Users\\Administrator\\Desktop\\ppp.xlsx",header=None)
a=dt.values
h=a[:,::2]
w=a[:,1::2]
h=reshape(h,(-1,1))
w=reshape(w,(-1,1))

plt.rc('font',size=16)
plt.rc('font',family='SimHei')

W=plt.hist(w,20,density=True,histtype='step',cumulative=True)  #histtype='step':阶梯函数  ='bar'：填充与x轴间的空间,同=stepfilled
print(W)
#plt.grid()     #添加辅助线
plt.savefig('fig4_11.png',dpi=500)
plt.show()
