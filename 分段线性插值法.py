#分段线性插值法

def P(x,y,a):
    for i in range(len(y)-1):
        if((x[i]<a)&(x[i+1]>a)): return (a-x[i])*y[i+1]/(x[i+1]-x[i])+(a-x[i+1])*y[i]/(x[i]-x[i+1])

x=[1,2,3,4]
y=[1,2,4,4]
a=2.5

print(P(x,y,a))

#仅在已知数值范围内适用（精确度高度依赖于已知数值对数量）