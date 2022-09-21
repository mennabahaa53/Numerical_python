import sympy as sym
global equation
global dequation
eps = float(input("enter eps:"))
x=sym.symbols("x")

equation=input("enter the equation:")

def equation_simplify(eq):
    global x
    simplifiedEquation = eq.strip()
    simplifiedEquation = simplifiedEquation.replace('x', '*x')
    
    if simplifiedEquation[0] == '*':
        simplifiedEquation = simplifiedEquation.replace('*', '')
        
    equation_list = []
    equation_list[:0] = simplifiedEquation # Seprate each character into an item in a list
    
    # Remove extra spaces in the equation if exists
    if ' ' in equation_list:
        equation_list.remove(' ')
    
    for i in range(len(equation_list)):

        if (equation_list[i] == '+' or equation_list[i] == '-') and equation_list[i+1] == '*':
            equation_list[i+1] = ''
            
    simplifiedEquation = ''.join(equation_list) # Concatenate all list items to equation
    simplifiedEquation = simplifiedEquation.replace('^', '**')
    return sym.sympify(simplifiedEquation)
equation=equation_simplify(equation)

def f(value):
    return round(float(equation.subs(x,value)),3)

def secant(ximinus1,x0):
    iter = 0
    print("iteration=", iter, "|xi-1=", ximinus1, "|f(Xi-1)=",f(ximinus1),"|xi=",x0,"|f(xi)=",f(x0),"error=","null")
    
    iter=1
    xi=x0
    xiplus1=xi-((f(xi)*(ximinus1-xi))/(f(ximinus1)-f(xi))) 
    ximinus1=xi
    error = abs((xiplus1 - xi) / xiplus1) * 100
    print("iteration=", iter, "|xi-1=", ximinus1, "|f(Xi-1)=",f(ximinus1),"|xi=",xiplus1,"|f(xi)=",f(xiplus1),"error=",round(error,3))
    while True:
       
        iter += 1
        xi=xiplus1
        xiplus1=xi-(f(xi)*(ximinus1-xi))/(f(ximinus1)-f(xi))
        ximinus1=xi
        error = abs((xiplus1 - xi) / xiplus1) * 100
        print("iteration=", iter, "|xi-1=", ximinus1, "|f(Xi-1)=",f(ximinus1),"|xi=",xiplus1,"|f(xi)=",f(xiplus1),"error=",round(error,3))


        if error < eps:
            return round(x0,3)
        
ximinus1 = float(input("enter xi-1 :"))
x0=float(input('enter x0:'))

root = secant(ximinus1,x0)
print("root=", root)