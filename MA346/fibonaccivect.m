function ret = fibonaccivect(n)
% Calculates the first n fibonacci numbers starting from 0 and 1 as the 0th
% and 1st numbers
nums = 1:n;
ret = (1 / sqrt(5)) * (((1 + sqrt(5)) / 2).^nums - ((1 - sqrt(5)) / 2).^nums);
ratio = ((1 / sqrt(5)) * (((1 + sqrt(5)) / 2).^nums - ((1 - sqrt(5)) / 2).^nums))./((1 / sqrt(5)) * (((1 + sqrt(5)) / 2).^(nums - 1) - ((1 - sqrt(5)) / 2).^(nums - 1)))