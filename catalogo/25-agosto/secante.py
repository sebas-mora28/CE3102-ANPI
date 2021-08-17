import sympy as sp



def secante(f, x0, x1, tol, iterMax):



    x = sp.Symbol('x')
    f1 = sp.sympify(f)

    xk = x0
    xk1 = x1
    error = tol + 1
    k = 1
    

    while (error >= tol and  k <= iterMax):
    


        
        d = sp.N(f1.subs(x, xk1)) - sp.N(f1.subs(x, xk))

        if(d == 0):
            break
        
        temp = xk1
        xk1 = xk1 - ((xk1 - xk)/d)*sp.N(f1.subs(x, xk1))
        print(xk1); 
        k += 1
        xk = temp
        error = abs(sp.N(f1.subs(x, xk1)))
        print(xk1)
    


    return [xk1, error]






f = 'x**2 - 2'
x0 = -1
x1 = 10
tol = pow(10, -5)
iterMax = 10000; 

y = secante(f, x0, x1, tol, iterMax)
print(y)

 


