import sympy as sym
global equation
eps = float(input("enter eps :"))
x=sym.symbols("x")

equation=input("enter the equation:")

def equation_simplify(x): 
    simpliEquation = equation.strip()
    simpliEquation = simpliEquation.replace('x', '*x')
       
    if simpliEquation[0] == '*':
           simpliEquation = simpliEquation.replace('*', '')
       
    for i in range(len(simpliEquation)-1):
         if i == len(simpliEquation)-1:
              break
           
         if simpliEquation[i] == '+' and simpliEquation[i+1] =='*':
               simpliEquation = simpliEquation.replace('*', '')
           
    simpliEquation = simpliEquation.replace('^', '**')
       
    simpliEquation=sym.simplify(simpliEquation)
    return simpliEquation
equation=equation_simplify(equation)
def f(value):
    return round(float(equation.subs(x,value)),3)
#-2+7x-5x^2+6x^3    
#eps=10
#xl=0
#xu=11
def bisect(xl, xu):
    iter = 1
    xr = 0
    xrold = 0
    error = 0
    while True:
        xrold = xr
        xr = (xl + xu) / 2
        error = abs((xr - xrold) / xr) * 100
        print("iteration=", iter, "|x1=", xl, "|f(xl)=", f(xl), "|xu=", xu, "|f(xu)=", f(xu), "|xr=", xr, "|f(xr)=",
              f(xr))
        if iter==1 :
            print("error%=","null")
        else:
            print("error%=",round(error,3),'%')
            

        if f(xl) * f(xr) > 0:
            xl = xr
        else:
            xu = xr
        iter += 1
        

        if error < eps:
            return xr
xl = float(input("enter lower value="))
xu = float(input("enter upper value="))
if f(xl) * f(xu) < 0:
    root = bisect(xl, xu)
    print("root=", root)
else:
    print("this equation has no answer")
