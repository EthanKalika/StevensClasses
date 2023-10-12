function ret = fibonacci(n)
% Calculates the first n fibonacci numbers starting from 1 and 1 as the 0th
% and 1st numbers
num1 = 1;
num2 = 1;
if (n < 1)
    % Notifies if input is too small
    disp("Invalid input")
elseif (n > 2)
    % Performs all calculations
    disp("F1: " + num1)
    disp("F2: " + num2)
    disp("ratio: " + num2 / num1)
    for index = 3:n
        numint = num2;
        num2 = num1 + num2;
        num1 = numint;
        disp("F" + index + ": " + num2)
        disp("ratio: " + num2/num1)
    end
elseif (n == 1)
    % Prints out results if the user enters 1
    disp("F1: " + num1);
    disp("ratio: No ratio because there is only 1 term")
else
    % Prints out results if the user enters 2
    disp("F1: " + num1);
    disp("F2: " + num2);
    disp("ratio: " + num2/num1)
end