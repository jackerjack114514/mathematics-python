#需要安装cvxpy凸优化库

import cvxpy as cp
import numpy as np
import pandas as pd
d1=pd.read_excel("C:\\Users\\Administrator\\Desktop\\Pdtaa5_6.xlsx",header=None)
d2=d1.values
d=d2[-1,:-1].reshape(1,-1)
e=d2[:-1,-1].reshape(-1,1)
x=cp.Variable((6,8))
obj=cp.Minimize(cp.sum(cp.multiply(c,x))) #目标函数

con=[cp.sun(x,axis=1,keepdims=True)<=e,cp.sum(x,axis=0,keepdims=True)==d,x>0]
prob=cp.Problem(obj,con)
prob.solve(solver='GLPK_MI',verbose=True)
print(prob.value,'\n\n')    #最优值
print(x.value)     #最优解
