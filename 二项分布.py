#Binomial Probability:二项分布

from scipy.stats import binom
n,p=20,0.8    #X~b(20,0.8)
print(binom.stats(n,p))  #输出均值与方差

print(binom.stats(n,p,moments='mvsk')) 
#依次输出mean(均值),variance(方差),skewness(偏度),kurtosis(峰度)
#"mvsk"的排列顺序不影响输出顺序



