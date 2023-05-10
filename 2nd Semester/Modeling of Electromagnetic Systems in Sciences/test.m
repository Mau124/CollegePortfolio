% Este documento prueba los disintos metodos numericos
func = @(x, y) cos(x) + sin(x).*cos(x);
dfunc = @(x, y) (-1)*sin(x)+cos(2.*x);

x = 0:0.01:8;
y = func(x);
dy = dfunc(x);

hold on
plot(x, y, 'b'), xlabel('x'), ylabel('f(x)'), grid on, title('Test')

[xpoints, ypoints] =rk_main(dfunc, @eulerInt, 1, 0, 8, 0.1, 0.1);
[xpoints2, ypoints2] = rk_main(dfunc, @ralstonInt, 1, 0, 8, 0.1, 0.1);
[xpoints3, ypoints3] = rk_main(dfunc, @rk_4, 1, 0, 8, 0.1, 0.1);

% plot(xpoints, ypoints, 'r');
% plot(xpoints2, ypoints2, 'y');
% plot(xpoints3, ypoints3, 'g');