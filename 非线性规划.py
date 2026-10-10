#非线性规划 
#min((2+x1)/(1+x2)-3x1+4x3)
#s.t. 0.1<=xi<=0.9 i=1,2,3

from scipy.optimize import minimize
from numpy import ones
def obj(x):
    x1,x2,x3=x
    return (2+x1)/(1+x2)-3*x1+4*x3

LB=[0.1]*3
UB=[0.9]*3

bound=tuple(zip(LB,UB))
ans=minimize(obj,ones(3),bounds=bound)  #ones(3) 为初值 ,obj无需传参

print(ans.fun,'\n',ans.success,'\n',ans.x)