import pandas as pd
import numpy as np

s=pd.Series([10.5,20.5,90],index=['a','b','c'])
a=s['b']
b1=np.mean(s)
b2=s.mean()
print(b1,b2)

a=np.random.randint(0,100,[10,10])
a=a.reshape(-1,1)
print(a,"\n\n\n")
df1=pd.DataFrame(a)
print(df1.describe())

#df2=pd.DataFrame(a,index=['a','b','c'],columns=['x1','x2'])
#df3=pd.DataFrame({'x1':a[:,0],'x2':a[:,1]})
#print(df1,"\n\n",df2,"\n\n",df3)
print("df1.count():{}\n\ndf1.mad()={}\n\ndf1.mode()={}\n\ndf1.skew={}\n\ndf1.kurt={}\n\ndf1.quantile={}".format(df1.count(),df1.mad(),df1.mode(),df1.skew(),df1.kurt(),df1.quantile()))
#count:非NaN数据项个数
#mad：中位数绝对偏差
#mode：众数
#skew：偏度，反映分布的对称性。均值右侧数据多于左侧时称为右偏态，左侧数据多于右侧时称为左偏态。接近0时，可认为分布是对称的。
#kurt：峰度，反映分布形状。正态分布的峰度为3，若数据峰度远大于3，则表示分布有沉重的尾巴，样本中含有较多远离均值的数据，可用作衡量偏离正态分布的尺度之一。
#quantile：样本分位数，默认为50%分位数