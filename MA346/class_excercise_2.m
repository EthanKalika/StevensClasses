x = [-2 3 1 0 4];
y = [9 0 7 0 0];
z = [-4 6 2 0 8];

x > 2 & x < 8 & y <= 0
% This does run, it compares consecutive elements of the array using the
% predicate expression


x <= 1;
y(x <= 1)
% This does run it returns the elements of y for which the corresponding
% elements of x are less than or equal to 1

z((x <= 2) | (y >= 4))
% This returns the elements of z for which the boolean expression is true