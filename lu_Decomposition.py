import numpy as np
from numpy import array,zeros

a=np.array([[float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))]],float)

b=np.array([float(input("x1=")),float(input("x2=")),float(input("x3="))],float)

n=len(b)  #to define the length of the system
x=zeros(n,float)

#calculate lc=b
l=array([[1,0,0],
         [a[1,0]/a[0,0],1,0],
         [a[2,0]/a[0,0],a[1,2]/a[1,1],1]])
c=zeros(n,float)
c[n-1]=b[n-1]/l[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ac=0
    for j in range(i+1,n):
        sum_ac+=l[i,j]*c[j]
    c[i]=(b[i]-sum_ac)/l[i,i]
print('the solution of the system is:',c)
print("|c1=",c[0],"|c2=",c[1],"|c3=",c[2])

#calculate ux=c
# k for column , i for row
for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k]==0:
            continue
        factor = a[k,k]/a[i,k] #a(2,1)[1]=a(1,1)[0]-a(2,1)[0]
        for j in range(k,n):
            a[i,j]=a[k,j]-a[i,j]*factor 
        b[i]=b[k]-b[i]*factor
u=a
x[n-1]=c[n-1]/u[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ux=0
    for j in range(i+1,n):
        sum_ux+=u[i,j]*x[j]
    x[i]=(c[i]-sum_ux)/u[i,i]
print('the solution of the system is:',x)
print("|x1=",x[0],"|x2=",x[1],"|x3=",x[2])
