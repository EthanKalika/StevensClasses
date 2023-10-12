% This function calculates the gausian elimination of the matrix resulting
% when the n*1 vector b is appended to the left of the n*n matrix A. The
% assuption for A is the pivoting is not needed.
function GE = gauss_elim(A, b)
% Checks the size of A and returns an error if A is not square
s = size(A);
if (s(1) ~= s(2))
    GE = "error"
else
    % Loops over the lower triangle of the matrix and performs necessary
    % calculations to cancel needed terms
    n = s(1);
    C = cat(2, A, b);
    for i = 1:(n - 1)
        for j = (i + 1):n
            if C(j, i) ~= 0
                C(j, :) = C(j, :) - (C(j, i) / C(i, i)) * C(i, :)
            end
        end
    end
    % Performs back substitution to solve for x
    for k = (n:-1:1)
        GE(k) = C(k, n + 1);
        sub = 0;
        for z = (n - 1:-1:k)
            sub = sub + C(k, z + 1) * GE(z + 1);
        end
        GE(k) = (GE(k) - sub) / C(k, k);
        GE = GE';
    end
end