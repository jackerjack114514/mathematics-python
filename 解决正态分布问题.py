from scipy.integrate import quad
from numpy import exp,sqrt,pi,abs
a=80;b=0.02;BD=a/b;mu=4000;s=100
y=lambda x:x*exp(-(x-mu)**2/(2*s**2))/sqrt(2*pi)/s #cdf

I=0;x1=0;x2=10000
while abs(I-BD)>1E-16:
    c=(x1+x2)/2
    I=quad(y,-10000,c)[0]
    if I>BD:x2=c
    else:x1=c
print(c)