import numpy as np
import pandas as pd
a=np.loadtxt("C:\\Users\\Administrator\\Desktop\\Pdata9_1_1.txt")
R1=a.copy();R2=a.copy();R3=a.copy()

for j in [0,1,2,4,5]:
    R1[:,j]=R1[:,j]/np.linalg.norm(R1[:,j])  #向量归一
    R2[:,j]=R1[:,j]/max(R1[:,j])
    R3[:,j]=(R3[:,j]-min(R3[:,j]))/(max(R3[:,j])-min(R3[:,j]))  #比例变换

R1[:,3]=1-R1[:,3]/np.linalg.norm(R1[:,3])
R2[:,3]=min(R2[:,3])/R2[:,3]
R3[:,3]=(max(R3[:,3])-R3[:,3])/(max(R3[:,3])-min(R3[:,3]))


np.savetxt("C:\\Users\\Administrator\\Desktop\\Pdata9_1_2.txt",R1)
np.savetxt("C:\\Users\\Administrator\\Desktop\\Pdata9_1_3.txt",R2)
np.savetxt("C:\\Users\\Administrator\\Desktop\\Pdata9_1_4.txt",R3)

DR1=pd.DataFrame(R1)
DR2=pd.DataFrame(R2)
DR3=pd.DataFrame(R3)

f=pd.ExcelWriter('C:\\Users\\Administrator\\Desktop\\Pdata9_1_5.xlsx')
DR1.to_excel(f,'sheet1')
DR2.to_excel(f,'sheet2')
DR3.to_excel(f,'sheet3')
f.save()

