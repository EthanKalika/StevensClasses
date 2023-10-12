% Create function
function invSum = invSum(N)

% Write code for function
invSum = single(0.0);

for i = 1:N
    invSum = invSum + single(1.0)/single(i);
end