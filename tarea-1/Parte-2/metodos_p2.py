import sympy as sp


def newton_H_m1(fun, x0, tol, iterMax):

    # Se escoge el metodo Newton donde H(u) = 1

    x = sp.Symbol('x')
    f1 = sp.sympify(fun)
    df1 = sp.diff(f1, x)
    error = tol + 1
    k = 1
    xk = x0
    h = 1


    while (error >= tol and k <= iterMax):

        n = sp.N(f1.subs(x, xk))
        d = sp.N(df1.subs(x, xk))

        if d != 0 and abs(d) < 10**-15:
                break

        xk = xk - h*(n/d)

        error = abs(f1.subs(x, xk))
        k += 1
        
    return [xk, k, error]


def newton_H_m2(fun, x0, b, tol, iterMax):

    x = sp.Symbol('x')
    f1 = sp.sympify(fun)
    df1 = sp.diff(f1, x)
    error = tol + 1
    k = 1
    xk = x0

    while (error >= tol and k <= iterMax):

        n = sp.N(f1.subs(x, xk))
        d = sp.N(df1.subs(x, xk))

        h = (1/(1+ b*(n/d)))
        xk = xk - h*(n/d)

        if d != 0 and abs(d) < 10**-15:
                break

        error = abs(f1.subs(x, xk))
        k += 1
        
    return [xk, k, error]






f = 'exp(x) - 1/x'
x0 = 1
tol = 10**-19
iterMax = 10000
b = 0

y = newton_H_m1(f, x0, tol, iterMax)
y2 = newton_H_m2(f, x0, b, tol, iterMax)
print(y)
print(y2)