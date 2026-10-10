#上α分位数 分布F(x)中,P(X>xa)=α时，称xa为该分布的上α分位数

from scipy.stats import norm
from pylab import plot,fill_between,show,text,legend,savefig,rc
from numpy import array,linspace,zeros

alpha=array([0.001,0.005,0.01,0.025,0.05,0.10])
za=norm.ppf(1-alpha,0,1) #Percentage Point Function，求下α分位数，故取1-α为上α分位数 
print(za,"\n")
x=linspace(-4,4,100)
y=norm.pdf(x,0,1)  #Probability Density Function, norm.pdf(x,0,1)生成标准正态分布
plot(x,y)
x2=linspace(za[-1],4,100)
y2=norm.pdf(x2)
y1=[0]*len(x2)

fill_between(x2,y1,y2,color='r')  #fill_between 填充两曲线间的空间 （Fill between two sets of y-values.）
plot([-4,4],[0,0])
#text(1.9,0.07,"$\\leftarrow\\alphas$=0.1")
savefig('fig.png',dpi=500)
show()

