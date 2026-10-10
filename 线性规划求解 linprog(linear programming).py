#线性规划求解 linprog(linear programming)
#res=linprog(c,A,b,Aeq,beq)
#res=linprog(c,A=None,b=None,Aeq=None,beq=None,bounds=None,method='simplex')
#c为价值向量， x为返回变量的取值，fval为返回目标函数的最优值，
# A和b对应线性不等式约束(严格小于)，Aeq和beq对应线性等式约束，lb和ub为变量的下界和上界向量。
#标准型： z=c.Tx (min)
#s.t. {A.x<b
#      Aeq*x=beq
#      Lb<=x<=Ub}

from scipy.optimize import linprog
c=[-1,4];A=[[-3,1],[1,2]];b=[6,4]
bound=((None,None),(-3,None))
res=linprog(c,A,b,None,None,bound)
print(res.fun)  #最小值
print(res.x)    #最优解

c=[-1,2,3];A=[[-2,1,1],[3,-1,-2]];b=[9,-4];Aeq=[[4,-2,-1]];beq=[-6];bound=[[-10,None],[0,None],[None,None]]
res=linprog(c,A,b,Aeq,beq,bound)
print(res.fun)  #最小值
print(res.x)    #最优解

#P.S.列表元素无法取相反数，故可利用数组array编写，方便交换max与min对应的标准型
#务必按照标准格式输入数据