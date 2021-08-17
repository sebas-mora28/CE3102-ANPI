function ejemplo_newton_raphson()
  clc; clear; 
  %Calcular el cero de exp(x)-2*x-10=0
  %Paso 1: Conocer el intervalo donde 
  %        se encuentra el cero
  %        Sugerencia: graficar la funcion
  %        f(x)=exp(x)-2*x-10
  
  %xv=-5:0.1:5;
  %yv=exp(xv)-2*xv-10;
  %plot(xv,yv)
  %grid on
  
  %Concluimos que la funcion tiene un cero 
  %en el intervalo [2,4]
  f='1/x';
  x0 = 5;
  tol=10^-9;
  iterMax=1000;
  [xk error]= newton_raphson(f, x0, tol, iterMax)
  
end

function [xk error]= newton_raphson(f,x0, tol, iterMax)
%Esta funci�n aproxima la soluci�n de la ecuaci�n f(x)=0, 
%utilizando el m�todo de la bisecci�n
    %
    %Sintaxis:  [xk k error]= newton_raphson(f, x0, tol, iterMax)
    % 
    %Parametros Iniciales: 
    %            f = una  cadena de caracteres (string) que representa a la funci�n f
    %            x0 = valor inicial 
    %            tol = un n�mero positivo que representa a la tolerancia para el criterio |f(xk)|<tol
    %            iterMax = cantidad de iteraciones m�ximas
    %            
    %Parametros de Salida:                           
    %            xk = aproximaci�n del cero de la funci�n f
    %            k = n�mero de iteraciones realizados
    %            error =  |f(xk)|
    %%%% Se debe instalar el paquete Symbolic
    %%%% Paso 1: Descargar el archivo symbolic-win-py-bundle-2.9.0.tar.gz
    %%%%         de la pagina https://github.com/cbm755/octsympy/releases
    %%%% Paso 2: Escribir en la Venta de Comandos de Octave la instruccion
    %%%%         pkg install symbolic-win-py-bundle-2.9.0.tar.gz  
    
    %%% Cargar el paquete symbolic
    
    warning('off', 'all');
    pkg load symbolic
    f1=matlabFunction(sym(f));
    diff_f1 = matlabFunction(diff(sym(f))); %Derivada de una funci�n
    error = tol + 1;
    k = 0;
    xk = x0; %Valor inicial del xk, obtenidos a partir de los argumentos de la funcion
    err = [];
    
    while (error > tol && k < iterMax) 
      
      n = f1(xk); %Se evalua la funcion en xk
      d = diff_f1(xk); %Se evalua la derivada de la funcion en xk
      
      if (d ~= 0 & abs(d) < 10**-15)
        break;
      endif
      
      xk = xk - n/d; %Nuevo valor del xk utilizando la formula xk - f(x)/f'(x) 
      error = abs(f1(xk)); % Calculo del error
      err = [err error];
      k = k + 1;
      
      plot(0:length(err)-1,err,'g','LineWidth',2)
      title('Grado del Polinomio vrs Error Relativo')
      xlabel('Grado del Polinomio (k)')
      ylabel('Error Relativo')

      
      
    endwhile
    
    
    
end
