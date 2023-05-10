% Funcion para el metodo de Euler
% Mauricio Andres Flores Perez - A01639917

function [x, y]= eulerInt(eq, x_ini, y_ini, h)
    y = y_ini+eq(x_ini, y_ini)*h;
    x = x_ini+h;
end
