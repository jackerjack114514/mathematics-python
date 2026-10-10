import sympy as sp
from sympy.abc import h
from sympy import *

t=sp.symbols('t',cls=sp.Function)
g=9.8
eq=sp.diff(t(h),h)-10000*sp.pi/(0.62*sp.sqrt(2*g))*(h**(3/2)-2*h**(1/2))

t=sp.dsolve(eq,ics={t(1):0})
t=sp.simplify(t)
print(t.args[1].n(9))

