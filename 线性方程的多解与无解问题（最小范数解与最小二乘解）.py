#无论数学上是否存在解，或者是多解，
#求解命令x=pinv(A).dot(b)总给出唯一解。
#pinv(A)为A的伪逆矩阵，满足Apinv(A)A=A

from numpy import array
from numpy.linalg import pinv
A=array([[1,1],[2,2],[1,2]])
b=array([1,3,2]);
b.resize(3,1)
x=pinv(A).dot(b)
print(x)    #原矛盾方程组无解，输出最小二乘解

A=array([[1,1,-3,-1],[3,-1,-3,-4],[1,4,-9,-8]])
b=array([1,4,0]);
b.resize(3,1)
x=pinv(A).dot(b)
print(x)    #原线性方程组有多解，输出最小范数解

