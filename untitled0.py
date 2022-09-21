import sympy as sym
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import sympy as sym
from numpy import array,zeros

root=Tk()
root.title('numerical project')
root.geometry('500x500')
#fg for text color , bg for label color,padx&pady for width and height of label
label1=Label(root,text='Chosse The Method...!',fg='white',bg='green',padx=10,pady=10).pack()
def solve_gauess_gorden():
    equation = fn_entry.get()
    xl = float(xl_entry.get())
    xu= float(xu_entry.get())
    eps = float(err_entry.get())
    equation = fix_equation(equation)
    
    a=array([[float(input("x1=")),float(input("x2=")),float(input("x3="))],
            [float(input("x1=")),float(input("x2=")),float(input("x3="))],
            [float(input("x1=")),float(input("x2=")),float(input("x3="))]],float)
 
    b=array([float(input("x1=")),float(input("x2=")),float(input("x3="))],float)
 
    n=len(b)  #to define the length of the system
    x=zeros(n,float)
    # k for column , i for row
    for k in range(n-1):
        for i in range(k+1,n):
            if a[i,k]==0:
                continue
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

    label_n = Label(root,text='root = '+str(xr))
    label_n.pack()
    
    
    
    
label_fn=Label(root,text='enter function')
fn_entry = Entry()
label_xl = Label(root, text='enter xl')
label_xu = Label(root, text='enter xu')
label_err = Label(root, text='enter error')
Button_cal = Button(root, text='calculate', command=solve_false_pos)
err_entry = Entry()

def false_pos():
    label_fn.pack()
    fn_entry.pack()
    label_xl.pack()
    xl_entry.pack()
    label_xu.pack()
    xu_entry.pack()
    label_err.pack()
    err_entry.pack()
    Button_cal.pack()
    arr.extend([label_fn,fn_entry,label_xl,label_xu,xl_entry,xu_entry,label_err,err_entry,Button_cal])

     

def show():
    delOld(arr)
    method = options.get()
    if method == 'False position':

        false_pos()
        


root = tk.Tk()
top = welcomeScreen(root) 
root.mainloop()