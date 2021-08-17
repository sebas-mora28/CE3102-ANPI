import numpy as np
import sympy as sp
import matplotlib.pylab as plt 



def metodo_secante(f, x0, x1, tol, iterMax):

    x = sp.Symbol('x')
    f1 = sp.sympify(f)
    error = tol + 1
    xk0 = x0
    xk1 = x1
    err = []
    k = 0
    xk_1 = 0


    while error>tol and k<iterMax:
        k += 1
        f_k0 = sp.N(f1.subs(x, xk0))
        f_k1 = sp.N(f1.subs(x, xk1))
        xk_1 = xk1 - ((xk1 - xk0)/(f_k1 - f_k0))*f_k1
        error = abs(xk_1 - xk1)/abs(xk_1)
        xk0 = xk1
        xk1 = xk_1 


    return [xk_1, k, error]



f = 'exp(-x^2) - x'
x0 = 0
x1 = 1
tol = 10**-2
iterMax = 10000

y = metodo_secante(f, x0, x1, tol, iterMax)
print(y)
