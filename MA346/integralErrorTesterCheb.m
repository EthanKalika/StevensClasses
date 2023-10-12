%% Intitialization of variables
mF = @myFunction;
intervalNums = [10, 20, 40, 80, 160];
keyVal = 2 / 3;
listOfTrapezErrors = [];
listOfSimpsonErrors = [];
%% Creation of arrays to plot
for i = intervalNums
    listOfBounds = [];
    for j = 0:i
        listOfBounds = [listOfBounds, (-1 * cos(j * pi / (2 * i)) + 1)];
    end
    listOfBounds
    listOfTrapezErrors = [listOfTrapezErrors, abs(trapez(mF, listOfBounds) - keyVal)];
    listOfSimpsonErrors = [listOfSimpsonErrors, abs(simpson(mF, listOfBounds) - keyVal)];
end
%% Plotting
loglog(intervalNums, listOfTrapezErrors);
hold on;
loglog(intervalNums, listOfSimpsonErrors);
legend('Trapezoidal Error', 'Simpson Error');
xlabel("log10(Partitions)")
ylabel("log10(Error)")
title("Errors of Integration Techniques")
hold off;
%% Calculation of least squares
pTrapezoidal = polyfit(log10(intervalNums), log10(listOfTrapezErrors), 1);
pSimpsons = polyfit(log10(intervalNums), log10(listOfSimpsonErrors), 1);
disp("Trapezoidal: The value of log(C) is " + string(pTrapezoidal(2)) + " and the value of k is " + string(pTrapezoidal(1)))
disp("Simpsons: The value of log(C) is " + string(pSimpsons(2)) + " and the value of k is " + string(pSimpsons(1)))