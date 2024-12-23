% Series combination of two resistors
series(R1, R2, Re) :-
    Re is R1 + R2.

% Parallel combination of two resistors
parallel(R1, R2, Re) :-
    Re is (R1 * R2) / (R1 + R2).

% Calculate the equivalent resistance of the given circuit
calculate_equivalent_resistance(Re) :-
    % First, calculate the resistance of 10 Ohm and 40 Ohm resistors in parallel
    parallel(10, 40, R3),

    % Then, add the 12 Ohm resistor in series with R3
    series(R3, 12, R4),

    % Finally, calculate the equivalent resistance of R4 in parallel with 30 Ohm
    parallel(R4, 30, Re).
