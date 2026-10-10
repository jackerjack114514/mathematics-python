#线性规划解决问题

from scipy.optimize import linprog

c=[110,120,130,110,115,-150]
A=[[1,1,0,0,0,0],[0,0,1,1,1,0],[-8.8,-6.1,-2.0,-4.2,-5.0,3],[8.8,6.1,2.0,4.2,5.0,-6]]
b=[200,250,0,0]
Aeq=[[1,1,1,1,1,-1]]
beq=[0]
bound=[[0,None],[0,None],[0,None],[0,None],[0,None],[0,450]]

ans=linprog(c,A,b,Aeq,beq,bound)
print(ans.fun)  #最优目标函数值
print(ans.x)  #保存决策变量最优值的数组
print(ans.nit)  #完成计算所需的迭代次数
print(ans.slack)  #松弛变量的值，即约束左右两侧的值之间的差异
print(ans.status) #此时slack两个分量均为0，说明两个约束条件均为紧约束，最优解使得不等式约束条件到达边界（等价于等式约束）
print(ans.success)  #是否已找到最佳解决方案
print(ans.message)  #解决方案的状态
print(ans.con)  #等式约束残差