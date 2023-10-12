function mySign = my_sign(n)
% Puts a string representing the sign of n into mySign
if (n > 0)
    mySign = "positive";
elseif (n < 0)
    mySign = "negative";
else
    mySign = "zero";
end