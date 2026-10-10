#矩阵基本操作
import sympy as sp,numpy as np
A=sp.Matrix(np.arange(1,17,dtype=int).reshape(4,4)) #4x4方阵
B=sp.eye(4) #单位矩阵

print("sp.det(A):",sp.det(A)) #行列式
print("A.rank(): ",A.rank()) #秩
print("A.transpose(): ",A.transpose()) #转置矩阵
print("A.T: ",A.T) #转置矩阵，同上
print("(A+10*B).inv(): ",(A+10*B).inv()) #逆矩阵
print("A**2: ",A**2) #矩阵平方
print("A*B: ",A*B) #矩阵乘法
print("A.row_join(B): ",A.row_join(B)) #横连矩阵
print("A.col_join(B): ",A.col_join(B)) #纵连矩阵
print("A[0:2,0:2]: ",A[0:2,0:2]) #提取子块
A2=A.copy();
A2.row_del(3)
print("A2: ",A2) #删除行

#解线性方程组
print("A.nullspace(): ",A.nullspace()) #基础解系
b=sp.Matrix([1,2,3,4])
C=A.row_join(b) #构造增广矩阵
print("C.reef(): ",C.rref()) #增广矩阵最简形
#由增广矩阵最简形可得通解

print("A.eigenvals(): ",A.eigenvals()) #特征值
print("A.eigenvects(): ",A.eigenvects()) #特征向量
print("A.diagonalizable(): ",A.is_diagonalizable) #判断矩阵能否对角化
print("A.diagonalize(): ",A.diagonalize()) #对角化矩阵

from numpy.linalg import eig
values,vectors=eig(A)  #eig(A)为含有两个矩阵的数组
print("values: ",values)  #特征值
print("vectors: ",vectors) #特征向量

#32行往后的代码有报错，暂未修复