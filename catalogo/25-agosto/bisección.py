import numpy as np
import sympy as sp
import matplotlib.pylab as plt 


def biseccion(f, a, b, tol, iterMax):
    """
    Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el 
    método de la bisección 


    - Sintaxis: y = biseccion(f, a, b, tol, iterMax)

    - Parámetros iniciales:
        f = cadena de caracteres (string) que representa a la funcion f
        a,b = son los extremos del intervalo [a, b]
        tol = un número positivo que representa a la tolerancia para el criterio |f(x) < tol|
        iterMax = cantidad de iteraciones máximas

    - Parámetros de salida:
        xk = aproximación del cero de la función
        k = número de iteraciones realizados 
        error = |f(xk)|

    Se deben instalar los paquetes numpy, sympy, matplotlib
    """

    x = sp.Symbol('x')
    f1 = sp.sympify(f)
    err = []
    xk = 0 

    f_a = sp.N(f1.subs(x, a))
    f_b = sp.N(f1.subs(x, b))


    if (f_a*f_b < 0): #se cumple la condición de Bolzano

        for k in range(1,iterMax): 

            xk = (a+b)/2 #Se tiene dos intervalos [a xk] [xk b]

            f_xk = sp.N(f1.subs(x, xk))
            
            if f_a*f_xk < 0: #Se cumple la condición en el intervalo 1
                b = xk

            else: #Se cumple la condición en el intervalo 2, es decir, [xk b]
                a = xk

            print(xk)
        

            error = abs(f_xk)
            err.append(error)
            if error < tol:
                break
        
        else:
            print("El intervalo seleccionado no cumple las condiciones de teorema de Bolzano")
            return [None, None, None]

        
        plt.rcParams.update({'font.size': 14})
        ejex=np.arange(1,k+1,1)
        fig, graf=plt.subplots()
        graf.plot(ejex,err,'b',marker='o',markerfacecolor='red',markersize=10)
        graf.set_xlabel('Iteraciones ($k$)')
        graf.set_ylabel('$|f(x_k)|$')
        graf.set_title('Metodo de biseccion (Iteraciones vrs Error)');
        graf.grid(True)
        plt.show()
        return [xk , k, error]


 
f = 'x^2 -2'
a = -1
b = 10
tol = 10**-5
iterMax = 10000

y = biseccion(f, a, b,  tol, iterMax)
print(y)

