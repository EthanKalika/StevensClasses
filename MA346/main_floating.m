% Compute the 30 values
set = [];
xvals1 = [];
setTwo = [];
setError = [];

for i = 1:30
    set(i) = invSum_Floating(2^i);
    xvals1(i) = 2^i;
    setTwo(i) = psi(2^(i) + 1) - psi(1);
    setError(i) = abs(set(i) - setTwo(i)) / abs(setTwo(i));
end

% Plot the error results
figure(1);
loglog(xvals1, setError)
xlabel("N")
ylabel("Error")

% whole thing again but counting backwards
sSet = [];
sSetTwo = [];
sSetError = [];
xvals2 = [];
for b = 1:30
    sSet(b) = invSum_Reverse(2^b);
    sSetTwo(b) = psi(2^(b) + 1) - psi(1);
    sSetError(b) = abs(sSet(b) - sSetTwo(b)) / abs(sSetTwo(b));
    xvals2(b) = 2^b;
end

% Plot the error again
figure(2);
loglog(xvals2, sSetError)
xlabel("N")
ylabel("Error")