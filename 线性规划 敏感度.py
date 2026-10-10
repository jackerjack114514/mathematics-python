from scipy.optimize import linprog
c=[-72,-64]
A=[[1,1],[12,8]]
b=[[50],[480]]
bound=[[0,100/3.0],[0,None]]

ans=linprog(c,A,b,None,None,bound,method='simplex',options={"disp":True})
print(ans.fun)  #最优目标函数值
print(ans.x)  #保存决策变量最优值的数组
print(ans.nit)  #完成计算所需的迭代次数
print(ans.slack)  #松弛变量的值，即约束左右两侧的值之间的差异  slack=B_ub-A_ubX,每一个分量对应一个约束式，若分量为0，说明最优解对应的约束条件为紧约束（等式约束），修改该约束条件边值会影响最优解
print(ans.status) #此时slack两个分量均为0，说明两个约束条件均为紧约束，最优解使得不等式约束条件到达边界（等价于等式约束）
print(ans.success)  #是否已找到最佳解决方案
print(ans.message)  #解决方案的状态
print(ans.con)  #等式约束残差

