#include <iostream>
#include <stdio.h>
#include <math.h>




double fun(double x)
{

    return pow(x, 2) - 2;

}


double* falta_posicion(double a, double b, int tol, int iterMax)
{

    /**
    Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el 
    método de la falsa posicion


    - Sintaxis: double* res = falta_posicio(a, b, tol, iterMax)

    - Parámetros iniciales:
        a,b = son los extremos del intervalo [a, b]
        tol = un número positivo que representa a la tolerancia para el criterio |f(x) < tol|
        iterMax = cantidad de iteraciones máximas

    - Parámetros de salida:
        xk = aproximación del cero de la función
        error = |f(xk)|

    */



    double x0 = a;
    double x1 = b;
    double f_a = fun(a);
    double f_b = fun(b);
    int k = 1;
    double error = tol + 1;

    if(f_a * f_b < 0) //Se verifica el teorema de Boltzam
    {

        x1 = x1 - (x1 - x0)/(fun(x1) - fun(x0)); //Se define el valor inicial de xk
    
        while (error > tol && k < iterMax ) //Se verifica el punto parada
        {
            double f_a = fun(a); //Se evalua la funcion en a
            double f_b = fun(b); //Se evalua la funcion en b
            double f_x1 = fun(x1); //Se evalua la funcion en x1 

            if (f_a * f_x1 < 0) //Se verifica el teorema de Boltzam con a y x1
            {
                b = x1; //Se asigna un nuevo valor de b
                double d = (fun(x1) - fun(a));
                if (d ==0)
                {
                    break;
                }
                x1 = x1 - ((x1 - a)/d) * fun(x1);
            }

            else if (f_b * f_x1 < 0) //Se verifica el teorema de Boltzam con a y x1
            {
                a = x1; //Se asigna un nuevo valor de b
                double d = (fun(x1) - fun(b));
                if (d ==0)
                {
                    break;
                }
                x1 = x1 - ((x1 - b)/d)*fun(x1);
            }
    
            error = abs(fun(x1)); //Se asigna el nuevo valor del error |f(xk)|
            k++;
        }

        double* res = (double*) malloc(sizeof(double)*2);
        res[0] = x1;
        res[1] = error; 

        return res;
    
    }

    return NULL;

}


int main()
{
    int a = -1;
    int b = 10;
    int tol = pow(10, -5);
    int iterMax = 10000;
    double* res = falta_posicion(a, b, tol, iterMax);
    printf("%f   %f  \n", res[0], res[1]);
    
}