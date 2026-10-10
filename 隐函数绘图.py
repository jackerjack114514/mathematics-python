import numpy as np
from sympy import Eq, plot_implicit as pt
import matplotlib.pyplot as plt
from scipy.integrate import *
from sympy.abc import x,y,z
from pylab import rc

pt(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4),xlabel='$x$',ylabel='$y$')
