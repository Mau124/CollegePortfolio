% Funcion para el metodo de Runge-Kutta de cuarto orden
% Mauricio Andres Flores Perez - A01639917

function [x, y] = rk_4(eq, x_ini, y_ini, h)
    k1 = eq(x_ini, y_ini);
    k2 = eq(x_ini+(1/2)*h, y_ini+(1/2)*k1*h);
    k3 = eq(x_ini+(1/2)*h, y_ini+(1/2)*k2*h);
    k4 = eq(x_ini+h, y_ini+k3*h);
    y = y_ini + (1/6)*h*(k1 + 2*k2 + 2*k3 + k4);
    x = x_ini + h;
end