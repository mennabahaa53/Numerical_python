#import numpy as np
from numpy import array,zeros,fabs

a=array([[float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))]],float)

b=array([float(input("x1=")),float(input("x2=")),float(input("x3="))],float)

n=len(b)  #to define the length of the system
x=zeros(n,float)
# k for column , i for row
for k in range(n-1):
    if fabs(a[k,k])<1.0e-12:
        for i in range(k+1,n):
            if fabs(a[i,k])>fabs(a[k,k]):
                a[[k,i]]=a[[k,i]]
                b[[k,i]]=b[[k,i]]
                break
    for i in range(k+1,n):
        if a[i,k]==0:continue
        factor = a[k,k]/a[i,k] #a(2,1)[1]=a(1,1)[0]-a(2,1)[0]
        for j in range(k,n):
            a[i,j]=a[k,j]-a[i,j]*factor 
        b[i]=b[k]-b[i]*factor
print(a)
print(b)

#back subsititution
x[n-1]=b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax=0
    for j in range(i+1,n):
        sum_ax+=a[i,j]*x[j]
    x[i]=(b[i]-sum_ax)/a[i,i]
print('the solution of the system is:',x)
print("|x1=",x[0],"|x2=",x[1],"|x3=",x[2])