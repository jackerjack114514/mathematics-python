import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


L=1.0;C=1.0  #参数：自感L，电容C
R_list=[0.5*(L*C)**0.5,2*(L*C)**0.5,5*(L*C)**0.5]  #欠阻尼/临界/过阻尼
print(list(R_list))
labels=['欠阻尼','临界阻尼','过阻尼']

t=np.linspace(0,20,1000)

def rlc(y,t,R):
    Q,I=y
    dQdt=I
    dIdt=-(R/L)*I-(1/(L*C))*Q
    return [dQdt,dIdt]  #电磁阻尼方程


#初始条件
y0=[1.0,0.0]

plt.figure(figsize=(8,5))
plt.rc('font',family='SimHei')
plt.rc('font',size=16)
plt.rc('axes',unicode_minus=False)


for R,lab in zip(R_list,labels):
    sol=odeint(rlc,y0,t,args=(R,))
    plt.plot(t,sol[:,0],label=lab)

plt.xlabel("时间")
plt.ylabel("电荷量 Q(t)")
plt.title("RLC电路的瞬态响应")
plt.legend()
plt.grid()

plt.savefig('C:\\Users\\Administrator\\Desktop\\1.png',dpi=500)

plt.figure(figsize=(18,6)) 

now=1
for R,lab in zip(R_list, labels):
    sol=odeint(rlc, y0, t, args=(R,))
    Q=sol[:,0]
    I=sol[:,1]

    UE=Q**2/(2*C)
    UB=0.5*L*I**2
    U=UE+UB
    plt.subplot(1,3,now)
    plt.plot(t, UE, '--', label=f'{lab} 电场能量')
    plt.plot(t, UB, ':', label=f'{lab} 磁场能量')
    plt.plot(t, U, label=f'{lab} 总能量')
    plt.xlabel("时间",size=16)
    plt.ylabel("能量",size=16)
    plt.legend(fontsize=12)
    plt.grid()

    if now==2:
        plt.title("RLC电路中的能量演化",size=24)
    now=now+1

plt.savefig('C:\\Users\\Administrator\\Desktop\\2.png',dpi=500)
plt.show()
