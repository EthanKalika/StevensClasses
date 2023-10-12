% This code compares code using a for loop with vectorized code 

% Define grid
t_grid = 0:.0000001:100;

% Allocate memory
y = zeros(1,length(t_grid));


tic; % Start time measurement
for i = 1:length(t_grid) 
    y(i) = sin(t_grid(i));
end
toc; % Stop time measurement

% Now we vectorize the code

tic; % Start time measurement
z = sin(t_grid);
toc; % Stop time measurement