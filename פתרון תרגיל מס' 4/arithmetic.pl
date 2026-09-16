% ==========================================
% Part 3: Arithmetic
% ==========================================

% 1.a Sum of numbers from 1 to N
scum(1, 1).
scum(N, Res) :- N > 1, N1 is N - 1, scum(N1, Res1), Res is Res1 + N.

% 1.b Sum of the digits of a number
sumDigits(0, 0).
sumDigits(Num, Sum) :- 
    Num > 0, 
    Digit is Num mod 10, 
    Num1 is Num // 10, 
    sumDigits(Num1, Sum1), 
    Sum is Sum1 + Digit.

% 2.a Split an integer into a list of its digits
split(0, [0]) :- !.
split(N, Res) :- N > 0, split_helper(N, [], Res).

split_helper(0, Acc, Acc).
split_helper(N, Acc, Res) :- 
    N > 0, 
    Digit is N mod 10, 
    N1 is N // 10, 
    split_helper(N1, [Digit|Acc], Res).

% 2.b Create a number from a list of digits (Leftmost is units)
create(List, N) :- create_helper(List, 1, 0, N).

create_helper([], _, Acc, Acc).
create_helper([H|T], Multiplier, Acc, N) :- 
    NewAcc is Acc + H * Multiplier, 
    NewMultiplier is Multiplier * 10, 
    create_helper(T, NewMultiplier, NewAcc, N).

% 2.c Reverse the digits of a number
reverse_digits(Num, NewNum) :- 
    split(Num, DigitsList), 
    create(DigitsList, NewNum).

% Helper for list operations
is_member_custom(X, [X|_]).
is_member_custom(X, [_|T]) :- is_member_custom(X, T).

% 3.a Intersection of two lists
intersection([], _, []).
intersection([H|T], L2, [H|Z]) :- is_member_custom(H, L2), intersection(T, L2, Z).
intersection([H|T], L2, Z) :- \+ is_member_custom(H, L2), intersection(T, L2, Z).

% 3.b Minus (Elements in L1 but not in L2)
minus([], _, []).
minus([H|T], L2, Z) :- is_member_custom(H, L2), minus(T, L2, Z).
minus([H|T], L2, [H|Z]) :- \+ is_member_custom(H, L2), minus(T, L2, Z).