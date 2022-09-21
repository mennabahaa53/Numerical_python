import sympy as sym

def fix_equation(equation):
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
       
    return simpliEquation



def f(equation,x_value):
    return round(eval(equation,{'x':x_value}),3)

def df(equation,x):
    eq = sym.diff(equation,sym.symbols('x'))
    return f(str(eq),x)

# -0.9*x^2+1.7*x+2.5
def newton(xo,eps,equation):
    iter = 0
    count = 0
    current_error = 0
    xi = xo
    xiold = 0
    xiplus1 = 0
    while True:
        current_error = abs(((xi - xiold) / xi) * 100)
        fx = f(equation,xi)
        dfx = df(equation,xi)
        print("iteration=", iter, "|xi=", xi, "|f(xi)=", fx, "|f`(xi)=", dfx)
        xiold = xi
        xi = round(xi - fx / dfx , 3)
        iter += 1
        if current_error <= eps and iter > 1:
            break

    return xi

# q=fix_equation('x+x^2+3*x+2')
# print(q)
# print(df(q,2))

#eps = float(input('enter epslon:'))
#equation = input("enter the equation:")
#xo = int(input("enter xo :"))

#print(newton(xo,eps,fix_equation(equation)))