% Problem 1
a = [5 -4 0];
b = [10 7 2];
A = [3 9 4; 18 5 0];

x = [A;b];
x = [A;b]\a'
% This is valid [A;b] appends b as the bottom row of A to get a 3 by 3
% matrix. Then it solves the system Ax=a^T.

b.*a
% This is valid and returns the element-wise multiplication of b and a

A+[a;b]
% This is valid and returns a matrix which is the sum of A and the matrix
% the rows of a and b

a.^b
% This is valid and returns a vector with elements of A to the power of the
% elements of b

% a*b does not work because you can't multiply a and b as matrices
% a'*b and a*b' work as matrix multiplication
% A + 5 works and adds 5 to every entry of A