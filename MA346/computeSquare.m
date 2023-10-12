function y = computeSquare(x)
y = x.^2;
f = @computeSquare
print(trapez(f, [0, 0.25, 0.5, 0.75, 1]))