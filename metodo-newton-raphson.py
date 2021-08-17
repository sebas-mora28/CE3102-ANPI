import numpy as np
import sympy as sp
import matplotlib.pylab as plt 


def newton_raphson(f, x0, tol, iterMax):

    x = sp.Symbol('x')
    f1 = sp.sympify(f)
    df1 = sp.diff(f1, x)
    error = tol + 1
    xk = x0
    err = []
    k = 0


    while error>tol and k<iterMax:

        n = sp.N(f1.subs(x, xk))
        d = sp.N(df1.subs(x, xk))
        if d != 0 and abs(d) < 10**-15:
                break
        xk = xk - n/d
        error = abs(f1.subs(x, xk))
        err.append(sp.N(error))
        k += 1
        

    
    fig ,graph = plt.subplots()
    ejex = np.arange(1, k+1, 1)
    graph.plot(ejex, err)
    plt.show()
    
    

    return [xk, k , error]



f = 'exp(x) - 1/x'
x0 = 1
tol = 10**-19
iterMax = 10000


y = newton_raphson(f, x0, tol, iterMax)
print(y)


