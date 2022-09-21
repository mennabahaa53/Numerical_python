import sympy as sym

def fix_equation(equation):
    simpliEquation = equation.strip()
    simpliEquation = simpliEquation.replace('^', '**')
    return simpliEquation.replace('*','**')


def f(equation,x_value):
    return eval(equation,{'x':x_value})

def df(equation,x):
    eq = sym.diff(equation,sym.symbols('x'))
    return f(str(eq),x)

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
        print("iteration=", iter, "|xi=", xi, "|f(xi)=", fx)
        xiold = xi
        xi = f(xiold)
        iter += 1
        print(current_error)
        if current_error <= eps and iter > 1:
            break



# q=fix_equation('x+x^2+3*x+2')
# print(q)
# print(df(q,2))

eps = float(input('enter epslon:'))
equation = input("enter the equation:")
xo = int(input("enter xo :"))

newton(xo,eps,fix_equation(equation))