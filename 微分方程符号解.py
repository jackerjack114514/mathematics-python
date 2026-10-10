from sympy import diff,dsolve,simplify,Function,symbols,sin
from sympy.abc import x

y=symbols('y',cls=Function)
#y=Function('y')

"""
eq=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)
con={y(0):0,diff(y(x),x).subs(x,0):1}
y=dsolve(eq,ics=con)
print(simplify(y))
"""

eq2=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)-sin(x)
con2={y(0):0,diff(y(x),x).subs(x,0):1}
y2=dsolve(eq2,ics=con2)
print(simplify(y2))
