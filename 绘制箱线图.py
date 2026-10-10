#箱线图，用于比较多个数据集的性质

import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("C:\\Users\\Administrator\\Desktop\\Pdata4_9.txt")
b=a.T
plt.rc('font',size=16)
plt.rc('font',family="SimHei")
plt.boxplot(b,labels=['女子','男子'])  #boxplot绘制箱线图 
plt.savefig('fig4_9.png',dpi=500)
plt.show()

