#一次线性微分方程组(Python基于一阶方程进行对常微分方程的数值求解，故高阶微分方程必须化成一阶方程组，通常采用龙格—库塔方法)

import sympy as sp
t=sp.symbols('t')
x1,x2,x3=sp.symbols("x1:4",cls=sp.Function)
x=sp.Matrix([x1(t),x2(t),x3(t)])
A=sp.Matrix([[2,-3,3],[4,-5,3],[4,-4,2]])
eq=x.diff(t)-A*x
s=sp.dsolve(eq,ics={x1(0):1,x2(0):2,x3(0):3})
print(s)
