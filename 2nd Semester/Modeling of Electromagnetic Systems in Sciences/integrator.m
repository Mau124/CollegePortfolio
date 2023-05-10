function [x_new,y_new] = integrator(eq, method, x, y, h, x_end)
    x_new = x;
    y_new = y;
    while x_new < x_end
        if (x_end - x_new) < h
            h = x_end - x_new;
        end
        [x_new, y_new] = method(eq, x_new, y_new, h);
    end
end

