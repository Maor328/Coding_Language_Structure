% ==========================================
% Part 2: Recursion and Lists
% ==========================================

% 1. Reverse a list
reverse_list([], []).
reverse_list([H|T], Z) :- reverse_list(T, RevT), append(RevT, [H], Z).

% 2. Member of a list
is_member(X, [X|_]).
is_member(X, [_|T]) :- is_member(X, T).

% 3. Palindrome list
palindrome(L) :- reverse_list(L, L).

% 4. Sorted list (non-decreasing order)
is_sorted([]).
is_sorted([_]).
is_sorted([X,Y|T]) :- X =< Y, is_sorted([Y|T]).

% 5. Permutation of a list
extract(X, [X|T], T).
extract(X, [H|T], [H|R]) :- extract(X, T, R).

permutation_list([], []).
permutation_list(L, [H|T]) :- extract(H, L, Remainder), permutation_list(Remainder, T).