#风投(固定收益时的最小风险)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

M=1000000;reward=200000

c=[0,0,0,0,0,1/M]  #s5=bank
A=[[0.025,0,0,0,0,-1],[0,0.015,0,0,0,-1],[0,0,0.055,0,0,-1],[0,0,0,0.026,0,-1],[-0.27,-0.19,-0.185,-0.185,-0.05,0],[1.01,1.02,1.045,1.065,1.005,0]]
b=[0,0,0,0,-reward,M]  

bound=[[0,None],[0,None],[0,None],[0,None],[0,None],[0,None]]
ans=linprog(c,A,b,None,None,bound)
print(ans.fun,ans.x)