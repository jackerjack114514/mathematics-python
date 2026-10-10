#理想解排序法/灰色关联度法/熵值法/秩和法

import numpy as np
from scipy.stats import rankdata

a=np.loadtxt('C:\\Users\\Administrator\\Desktop\\Pdata9_1_3.txt')

print('原始观测数据经比例变换法得到的评价矩阵:\n',a,'\n\n')

#TOPSIS法
print("-------------TOPSIS理想解排序法-------------\n")
cplus=a.max(axis=0)
cminus=a.min(axis=0)
print('正理想解:{}\n负理想解:{}'.format(cplus,cminus))
d1=np.linalg.norm(a-cplus,axis=1)
d2=np.linalg.norm(a-cminus,axis=1)
print("正理想解距离:{}\n负理想解距离:{}".format(d1,d2))
f1=d2/(d1+d2)
print("TOPSIS评价值:",f1,'\n\n')



#灰色关联度法
print("-------------灰色关联度法-------------\n")
t=cplus-a
mmin=t.min()
mmax=t.max()
rho=0.5  #分辨系数ρ=0.5
xs=(mmin+rho*mmax)/(t+rho*mmax)
f2=xs.mean(axis=1) #行均值
print('关联系数={}\n关联度={}'.format(xs,f2))
print("关联度排序：",np.sort(f2),'\n\n')


#熵值法
print("-------------熵值法-------------\n")
[n,m]=a.shape
cs=a.sum(axis=0)
P=1/cs*a #特征比重矩阵
e=-(P*np.log(P)).sum(axis=0)/np.log(n) #熵值
g=1-e #差异系数
w=g/sum(g) #差异加权
F=P@w
print('P={}\ne={}\ng={}\nw={}\nF={}\n'.format(P,e,g,w,F))



#RSR秩和法
print("-------------RSR秩和法-------------\n")
R=[rankdata(a[:,i]) for i in np.arange(6)] #求列的秩
R=np.array(R).T
print('秩矩阵：',R,'\n')
RSR=R.mean(axis=1)/n
print('RSR=',RSR)




