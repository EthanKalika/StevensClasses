% This function takes in f, a function handel or an array containing
% fucntion outputs and a vector x containung the boundary points of a
% partition of the interval of integration and outputs the simpson
% approximation of the integral of f over the union of x
function inte = simpson(f, x)
accumulator = 0;
multiplier = 0;
width = (x(length(x)) - x(1)) / (length(x) - 1);
% Case where f is a function handel
if isa(f, "function_handle")
    for i = 1:length(x)
        if ((i - 1) == 0 | (i - 1) == (length(x) - 1))
            multiplier = 1;
        elseif (mod((i - 1), 2) == 1)
            multiplier = 4;
        else
            multiplier = 2;
        end
        accumulator = accumulator + width * multiplier * f(x(i)) / 3;
    end
    inte = accumulator;
    % Case where f is an array
else
    for i = 1:length(x)
        if ((i - 1) == 0 | (i - 1) == (length(x) - 1))
            multiplier = 1;
        elseif (mod((i - 1), 2) == 1)
            multiplier = 4;
        else
            multiplier = 2;
        end
        accumulator = accumulator + width * multiplier * f(i) / 3;
    end
    inte = accumulator;
end