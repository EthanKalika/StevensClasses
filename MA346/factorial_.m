function factorial = factorial_(n)
% Calculates the factorial of n
num = 1;
for index = 1:n
    num = num * index;
end
factorial = num;