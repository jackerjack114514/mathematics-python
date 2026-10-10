import numpy as np
from scipy.integrate import tplquad 
f=lambda z,y,x:z*np.sqrt(x**2+y**2+1)
print('I= ',tplquad(f,0,2,lambda x:-np.sqrt(2*x-x**2),lambda x:np.sqrt(2*x-x**2),0,6))