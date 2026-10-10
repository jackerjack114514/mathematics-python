#函数n阶差商与牛顿插值法
#每增加一个节点，插值多项式只增加一项，便于递推运算，计算量远小于Lagrange插值
#只能计算单点处插值

x=[1,2,3,4,5,6,7,8]
y=[1,4,9,16,25,36,49,64]
a=4.5

def diff_quo(xi=[],fi=[]):
    if ((len(xi)>2)&(len(fi)>2)):return (diff_quo(xi[:len(xi)-1],fi[:len(fi)-1])-diff_quo(xi[1:len(xi)],fi[1:len(fi)]))/float(xi[0]-xi[-1])
    return (fi[0]-fi[1])/float(xi[0]-xi[1])

def ind(x,y,a,n):
    d=1.0
    for i in range(n):
        d=d*(a-x[i])
    return d

def newton(x,y,a):
    s=y[0]
    for i in range(0,len(y)):
        d=1.0
        for j in range(i+1):
            d=d*(a-x[j])
        print(i,d,diff_quo(x[:i+2],y[:i+2]))
        s=s+d*diff_quo(x[:i+2],y[:i+2])
    return s

#print(diff_quo(x[:8],y[:8]))
print(newton(x,y,a))