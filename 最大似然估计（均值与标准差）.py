#最大似然估计（均值与标准差）

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  #normal,正态分布函数
from numpy import reshape
import pandas as pd

dt=pd.read_excel('C:\\Users\\Administrator\\Desktop\\ppp.xlsx',header=None)
a=dt.values
h=a[:,::2]
h=h.reshape(-1,1)

mu=np.mean(h)
s=np.std(h)

print("样本均值:{}\n标准差:{}\n".format(mu,s))
print("假定身高服从正态分布，则极大似然估计值为：",norm.fit(h))
