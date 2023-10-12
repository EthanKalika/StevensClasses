% Calculates the harmonic sum in reverse

function sum = invSum_Reverse(N)
sum = single(0.0);
for i = N:-1:1
    sum = sum + single(1.0)/single(i);
end