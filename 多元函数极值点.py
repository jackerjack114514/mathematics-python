from scipy.optimize import minimize

f=lambda x1,x2:100*(x2-x1**2)**2+(1-x1)**2

x0=minimize(f,[2.0,2.0],method=Powell)
#method表示使用的算法，其取值可为：
# 'Nelder-Mead'、'Powell'、'CG'/'BFGS'、
# 'Newton-CG'、'L-BFGS-B'、'TNC' 、
# 'COBYLA'、 'SLSQP'、'trust-constr'、
# 'dogleg'、'trust-ncg'、'trust-exact'、
# 'trust-krylov'。

