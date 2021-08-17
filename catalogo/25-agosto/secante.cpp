#include <iostream>
#include <math.h>
#include <stdio.h>

double fun(double x)
{
    return pow(x,2) - 2;   

}

double* secante(int a, int b, int tol, int iterMax)
{

    /**
    Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el 
    método de la secante


    - Sintaxis: double* res = secante(a, b, tol, iterMax)

    - Parámetros iniciales:
        a,b = son los extremos del intervalo [a, b]
        tol = un número positivo que representa a la tolerancia para el criterio |f(x) < tol|
        iterMax = cantidad de iteraciones máximas

    - Parámetros de salida:
        xk = aproximación del cero de la función
        error = |f(xk)|

    */


    double xk = a;
    double xk1 = b;
    double error = tol + 1;
    int k = 1; 

    while (error >= tol &&  k <= iterMax) // se verifica punto de parada
    {

        double d = fun(xk1) - fun(xk); //se obtiene el denominador de la formula de la secante

        if (d == 0) //Se verfica que el denominador no sea cero
        {
            break;
        }
        double temp = xk1; //Se almacena temporalmente el valor de xk1 para despues asignarlo a xk
        xk1 = xk1 - ((xk1 - xk)/d) * fun(xk1); //Se evalua la formula de la secante
        k++; //Se aumenta la iteracion 
        xk = temp; //Se actualiza el xk  
        error = abs(fun(xk1));
    }

    double* res = (double*) malloc(sizeof(double) *3);//Se intancia un array para almacenar las respuestas
    res[0] = xk1;
    res[1] = (double) k;
    res[2] = error;

    return res;


}



int main()
{

    int x0 = -1;
    int x1 = 10;
    double tol = pow(10, -5);
    int iterMax = 10000; 

    double* res = secante(x0, x1, tol, iterMax);
    printf("%f  %f  %f  \n", res[0], res[1], res[2]);

}
