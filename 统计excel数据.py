from numpy import *
import pandas as pd
df=pd.read_excel("C:\\Users\\Administrator\\Desktop\\ppp.xlsx",header=None) 
#要求列表为纯数据，否则excel读入时，a=df.values类型将是object而非可分析的float!!!

a=df.values
h=a[:,::2]  #奇数列，下标从0开始
w=a[:,1::2] #偶数列，下标从1开始
h=reshape(h,(-1,1)) #转换成列向量
w=reshape(w,(-1,1))
hw=hstack([h,w])

print([mean(h),median(h),ptp(h),var(h),std(h)]) #均值，中位数，极差，方差，标准差
print("cov:{}\ncorrcoef:{}".format(cov(hw.T)[0,1],corrcoef(hw.T)[0,1]))

