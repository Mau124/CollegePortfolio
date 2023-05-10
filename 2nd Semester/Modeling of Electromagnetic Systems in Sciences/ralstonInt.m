% Funcion para el metodo de Runge-Kutta de segundo orden - Ralston
% Mauricio Andres Flores Perez - A01639917

function [x, y] = ralstonInt(eq, x_ini, y_ini, h)
    a1 = 1/3;
    a2 = 2/3;
    p1 = 3/4;
    q11 = 3/4;
    k1 = eq(x_ini, y_ini);
    k2 = eq(x_ini + p1*h, y_ini + q11*k1*h);
    y = y_ini + h*(a1*k1 + a2*k2);
    x = x_ini + h;
end