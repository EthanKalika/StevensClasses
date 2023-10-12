% This function takes in a lower and upper bound and creates a polynomial
% approximation to the function 1/(1 + x^2) using the Chebyshev points
function LGP = lagrange_Polynomial_Cheb(lower, upper, n)
%% Creates a list of ordered pairs representing nodes
ls = [];
for i = 0:n
    node = cos(pi * i / n);
    node = (upper - lower) * node / 2 + (upper + lower) / 2;
    ls = [ls, [node, 1 / (1 + node^2)]];
end
%% Creates a list storing the lagrange basis
polyBasis = [];
for i = 1:2:(2 * n + 2)
    divisor = 1;
    poly = [1];
    for j = 1:2:(2 * n + 2)
        if (j ~= i)
            poly = conv(poly, [1, ls(j)]);
            divisor = divisor * (ls(j) - ls(i));
        end
    end
    polyBasis = [polyBasis, {ls(i + 1) * poly ./ divisor}];
end
%% Turns the lagrange basis into an interpolating polynomial
interpolant = zeros(size(poly));
for i = 1:(n + 1)
    interpolant = interpolant + polyBasis{i};
end
LGP = interpolant;