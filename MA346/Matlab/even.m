function a = even(n)

% This function determines whether a number is even.


if mod(n,2)==0
  a = 1;
  disp('The entered number is even.')
elseif mod(n,2)==1
  a = 0;
  disp('The entered number is odd.')
else
  a  = -1;  
  disp('The entered number is not an integer')
end