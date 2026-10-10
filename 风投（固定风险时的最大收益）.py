#风投(固定风险时的最大收益)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

M=1000000;risk=0.02

c=[-0.27,-0.19,-0.185,-0.185,-0.05]  #s5=bank
A=[[1.01,1.02,1.045,1.065,1],[0.025,0,0,0,0],[0,0.015,0,0,0],[0,0,0.055,0,0],[0,0,0,0.026,0]]
b=[M,M*risk,M*risk,M*risk,M*risk]  #M=100000 risk=0.03
bound=[[0,None],[0,None],[0,None],[0,None],[0,None]]

ans=linprog(c,A,b,None,None,bound)
print(ans.fun,ans.x)