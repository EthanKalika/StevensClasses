fplot(@(x) 1./(1 + x.^2))
ylim([-0.2, 1.2])
hold on;
fplot(@(x) polyval(lagrange_Polynomial_Cheb(-5, 5, 5), x))
fplot(@(x) polyval(lagrange_Polynomial_Cheb(-5, 5, 10), x))
fplot(@(x) polyval(lagrange_Polynomial_Cheb(-5, 5, 15), x))
xlabel('x')
ylabel('y')
title('Interpolation of f(x) using Lagrange Polynomials with Chebyshev Nodes')
legend('f(x)', 'n = 5', 'n = 10', 'n = 15')
hold off
% The interpolant for n = 5 is approximately 0x^5 + 0.0007x^4 - 0x^3 -
% 0.0293x^2 + 0x + 0.3614
% The interpolant for n = 10 is approximately: -0x^10 + 0x^9 + 0.0002x^8 -
% 0x^7 - 0.0062x^6 - 0x^5 + 0.0791x^4 - 0x^3 - 0.4519x^2 - 0x + 1
% The interpolant for n = 15 is approximately -0x^15 - 0x^14 + 0x^13 +
% 0x^12 - 0x^11 - 0.0001x^10 + 0x^9 - 0x^8 + 0.0012x^7 - 0x^6 - 0.0153x^5 +
% 0x^4 - 0x^3 - 0.4517x^2 - 0x + 0.9007