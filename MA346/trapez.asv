% This function takes in a function handle or vector of function outputs
% and an array containing boundary points for a partition of an
% interval and returns the integral of the given function over the union of
% the partition
function inte = trapez(f, x)
accumulator = 0;
if (isa(f, "function_handle"))
    % Case where we were given a function handel
    for i = 1:(length(x) - 1)
        accumulator = accumulator + ((x(i + 1) - x(i)) * (f(x(i + 1)) + f(x(i)))) / 2;
    end
    inte = accumulator;
else
    % Case where we were given a function vector
    for i = 1:(length(x) - 1)
        accumulator = accumulator + (x(i + 1) - x (i)) * (f(i + 1) + f(i)) / 2;
    end
    inte = accumulator;
end