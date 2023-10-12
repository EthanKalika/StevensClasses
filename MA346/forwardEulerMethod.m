% This function approximates the solution to the initial value problem
% y'(t) = -100y(t) + y^2(t) with y(0) = 1 and interval [0, 1] using the
% given step size variable h
function func = forwardEulerMethod(h)
x_val = 0;
x_vec = [x_val];
uCurr = 1;
accumulator = [uCurr];
while x_val < 1
    uCurr = uCurr * (1 - 100 * h) + h * uCurr^2;
    x_val = x_val + h;
    x_vec = [x_vec, x_val];
    accumulator = [accumulator, uCurr];
end
plot(x_vec, accumulator);
func = uCurr;