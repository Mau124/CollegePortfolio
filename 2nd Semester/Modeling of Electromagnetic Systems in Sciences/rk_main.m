function [xp,yp] = rk_main(eq, method, y, x_ini, x_fin, step, output_interval)
    x = x_ini;
    m = 1;
    elems = (x_fin - x_ini)/output_interval;
    xp = zeros(1, elems);
    yp = zeros(1, elems);
    xp(m) = x;
    yp(m) = y;
    while x < x_fin
        x_end = x+output_interval;
        if x_end > x_fin
            x_end = x_fin;
        end
        h = step;
        [x, y] = integrator(eq, method, x, y, h, x_end);
        m = m+1;
        xp(m) = x;
        yp(m) = y;
    end
end

