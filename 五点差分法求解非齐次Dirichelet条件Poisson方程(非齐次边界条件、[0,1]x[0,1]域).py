from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import diags, kron, eye 
from scipy.sparse.linalg import spsolve
import time

def solve_poisson_2d(N,M,f):  #五点差分,矩形网格剖分有N*M个内点
    h=1.0/(N+1)  #X
    k=1.0/(M+1)  #Y
    x_inner=np.linspace(h,1-h,N)
    y_inner=np.linspace(k,1-k,M)
    X,Y=np.meshgrid(x_inner,y_inner,indexing='ij')
    F=f(X,Y)
    b=F.reshape(N*M)

    main_diag_X=2.0*np.ones(N)
    off_diag_X=-1.0*np.ones(N-1)
    TX=diags([off_diag_X, main_diag_X, off_diag_X], offsets=[-1, 0, 1], format='csr') #一维差分矩阵 T1=tridiag(-1,2,-1)

    main_diag_Y=2.0*np.ones(N)
    off_diag_Y=-1.0*np.ones(N-1)
    TY=diags([off_diag_Y, main_diag_Y, off_diag_Y], offsets=[-1, 0, 1], format='csr') #一维差分矩阵 T2=tridiag(-1,2,-1)

    IX=eye(N, format='csr')
    IY=eye(M, format='csr')
    #此处扩容加入边界条件即可

    A=kron(IX,TX)/(h**2)+kron(TY,IY)/(k**2)  #二维五点差分矩阵 A(N*M)
    print(TX,TY)

    u_inner=spsolve(A,b)   #原Poisson方程离散形式对应线性方程组 Au=b
    U=np.zeros((N+2,N+2))  #扩容加入边界情形
    U[1:-1,1:-1]=u_inner.reshape((N,N))
    #此处加入边界条件


    x=np.linspace(0,1,N+2)
    y=np.linspace(0,1,N+2)

    return x,y,U

"""构造一具有解析解且满足Dirichelet边界条件的Poisson方程以校验五点差分法下步长对精度的影响:
u(x,y)=sin(pi x) sin(pi y)
-Δu=2*pi^2*sin(pi*x)sin(pi*y)"""

def f(x,y):
    return 2*np.pi**2*np.sin(np.pi*x)*np.sin(np.pi*y)

def g(x,y):
    return 2*x+2*y  #边界条件 

def u_exact(x,y):
    return f(x,y)


TIME=np.arange(1,100,1,dtype=float)
ERROR=np.arange(1,100,1,dtype=float)


"""
for i in range(1,100):
    start=time.time()
    N=10*i  #X轴方向内点数  #10*i
    M=10*i  #y轴方向内点数
    x,y,U=solve_poisson_2d(N,M,f)  #五点差分法求得矩形网格点上的离散数值解

    X_all,Y_all=np.meshgrid(x, y, indexing='ij')
    U_exact=u_exact(X_all,Y_all)  #矩形网格点上对应解析解的值


    end=time.time()
    error=np.max(np.abs(U-U_exact))
    
    TIME[i-1]=end-start
    ERROR[i-1]=error
    print("N={}  M={}  求解时间:{:.7f}秒  最大绝对误差{}".format(N,M,end-start,error))
    #print(f"最大绝对误差={error:.6e}")


#绘制划分数-消耗时间/绝对误差图
print(TIME,ERROR)
plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False) 
plt.figure(figsize=(12,8))

ARRAY=np.arange(10,1000,10)
plt.subplot(121)
plt.plot(ARRAY,TIME)
plt.xlabel("划分数")
plt.ylabel("消耗时间(秒)")
plt.title("")
plt.grid(True)

plt.subplot(122)
plt.plot(ARRAY,ERROR)
plt.xlabel("划分数")
plt.ylabel("绝对误差")
plt.title("")
plt.grid(True)

plt.subplots_adjust(wspace=0.5)
plt.savefig("C:\\Users\\Administrator\\Desktop\\划分数与时间消耗绝对误差图.png")
plt.show()
"""
x,y,U=solve_poisson_2d(100,100,f)
X_all,Y_all=np.meshgrid(x, y, indexing='ij')
U_exact=u_exact(X_all,Y_all)

plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False) 
plt.figure(figsize=(12,8))

#三维曲面图
ax=plt.subplot(121, projection='3d')
ax.plot_surface(X_all,Y_all,U,cmap='viridis')
ax.set_title("五点差分法求得Dirichlet条件下\nPoisson方程的数值解\n\n-Δu=2*pi^2*sin(pi*x)sin(pi*y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("u(x,y)")

#误差热图
ax=plt.subplot(122)
plt.imshow(np.abs(U-U_exact),origin='lower',extent=[0,1,0,1],aspect='auto')
plt.colorbar(label='Absolute Error')
plt.title("Absolute Error")
plt.xlabel("x")
plt.ylabel("y")
ax.set_aspect('equal')
plt.subplots_adjust(wspace=0.5)
plt.savefig("C:\\Users\\Administrator\\Desktop\\五点差分法求解Dirichlet条件齐次Poisson方程.png")
plt.show()