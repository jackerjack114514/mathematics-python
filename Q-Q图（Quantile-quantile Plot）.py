#Q-Q图 Quantile-quantile Plot（分位数-分位数图），确认经验分布与理论分布间的拟合效果
#将两者相同分位数点作为一个数组画在直角坐标中，n个观测数据对应n个点，图像越接近45°直线，说明拟合效果越好
#(需先进行参数估计)

#X~N(μ,σ^2) 此处讨论理论模型为正态分布的情形！

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,probplot
from numpy import *
import pandas as pd
dt=pd.read_excel("C:\\Users\\Administrator\\Desktop\\ppp.xlsx",header=None)
a=dt.values
h=a[:,::2] #height
h=h.flatten() #在此h.flatten（一维展开为行向量）并不等同于h.reshape(1,-1)或reshape(h,(1,-1)) 
#如h=[[1,2,3],[4,5,6],[7,8,9]],h.flatten()=[1,2,3,4,5,6,7,8,9],h.reshape(1,-1)=[[1,2,3,4,5,6,7,8,9]],格式不同

mu=np.mean(h);s=np.std(h)
print("mean(h)={}\nstd(h)={}".format(mu,s))

sh=np.sort(h)
n=len(sh)
xi=(np.arange(1,n+1)-1/2)/n
yi=norm.ppf(xi,mu,s)  ##Percentage Point Function，分布函数的反函数，用于求下α分位数

#利用pyplot绘制QQ图
plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc("axes",unicode_minus=False)
plt.subplot(121)
plt.plot(yi,sh,'o',label="QQ图")
plt.plot([100,220],[100,220],'r-',label='参考线')
plt.legend()

#直接调用库绘制QQ图
plt.subplot(122)
res=probplot(h,plot=plt)

plt.savefig('fig4_12.png',dpi=500)
plt.show()

#此处数据非正态分布，无法用上述模型拟合

