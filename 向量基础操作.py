import sympy as sp
A=sp.Matrix([[1],[2],[3]])
B=sp.Matrix([[4],[5],[6]])

print("A.norm():  ",A.norm()) #向量模长
print("A.norm().evalf():  ",A.norm().evalf()) #模长浮点数
print("A.T:  ",A.T) #转置矩阵
print("A.dot(B):  ",A.dot(B)) #点乘
print("A.cross(B):  ",A.cross(B)) #叉乘

from numpy import arange,cross,inner
from numpy.linalg import norm

print("inner(C,B): ",inner(A,B)) #内积，与点乘dot(A,B)等价

#一维数组可作行向量，可作列向量，故内积inner(a,b)与矩阵乘法dot(a,b)等价