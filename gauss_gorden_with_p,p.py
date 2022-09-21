import numpy as np
def gauss_gorden(a,b):
    a=np.array(a,float)
    b=np.array(b,float)
    n=len(b)
    for k in range(n):
        if np.fabs(a[k,k])<1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k])>np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j]=a[i,j],a[k,j]
                        b[k],b[i]=b[i],b[k]
                        break
        pivot=a[k,k]  
        for j in range(k,n):
            a[k,j]/=pivot
        b[k]/=pivot
        for i in range(n):
            if i==k or a[i,k]==0:
                continue
            factor=a[i,k]
            for j in range(k,n):
                a[i,j]-=factor*a[k,j]
            b[i]-=factor*b[k]
    return a,b
a=np.array([[float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))],
        [float(input("x1=")),float(input("x2=")),float(input("x3="))]],float)

b=np.array([float(input("x1=")),float(input("x2=")),float(input("x3="))],float)
X,A=gauss_gorden(a,b)

print("the solution :",X)
print("the transformation :",A)
print("|x1=",A[0],"|x2=",A[1],"|x3=",A[2])