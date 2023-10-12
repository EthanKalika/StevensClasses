fplot(@(x) 1./(1 + x.^2))
ylim([-0.2, 1.2])
hold on;
fplot(@(x) polyval(lagrange_Polynomial(-5, 5, 5), x))
fplot(@(x) polyval(lagrange_Polynomial(-5, 5, 10), x))
fplot(@(x) polyval(lagrange_Polynomial(-5, 5, 15), x))
xlabel('x')
ylabel('y')
title('Interpolation of f(x) using Lagrange Polynomials')
legend('f(x)', 'n = 5', 'n = 10', 'n = 15')
hold off
% The interpolant for n = 5 is approximately 0x^5 + 0.0019x^4 + 0x^3 -
% 0.0692x^2 - 0x + 0.5673
% The interpolant for n = 10 is approximately -0x^10 + 0x^9 + 0.0013x^8 -
% 0x^7 - 0.0244x^6 - 0x^5 + 0.1974x^4 - 0x^3 - 0.6742x^2 - 0x + 1
% The interpolant for n = 15 is approximately -0x^15 - 0x^14 + 0x^13 +
% 0x^12 + 0x^11 - 0.0006x^10 + 0x^9 + 0.0086x^8 + 0x^7 - 0.0693x^6 + 0x^5 +
% 0.3042x^4 + 0x^3 - 0.7192x^2 + 0x + 0.9762