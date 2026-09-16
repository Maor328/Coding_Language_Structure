% ==========================================
% Part 1: Family Relations
% ==========================================

% Base facts for testing
% Real family provided
male(yair).
male(yonatan).
male(ido).
male(maor).

female(maya).
female(liel).
female(hadar).
female(roni).
female(efrat).

% Fictional extended family for testing 3-4 generations
male(moshe).
male(haim).
male(shlomo).
male(dan).
female(rachel).
female(sara).
female(pnina).
female(michal).
female(tamar).

% Marriages (The man is always the first parameter)
married(yair, maya).
married(maor, efrat).
% Fictional marriages
married(moshe, rachel).
married(haim, sara).
married(shlomo, pnina).
married(yonatan, michal).

% Parent relations (Real family)
parent(yair, liel). parent(maya, liel).
parent(yair, hadar). parent(maya, hadar).
parent(yair, roni). parent(maya, roni).
parent(yair, yonatan). parent(maya, yonatan).
parent(yair, ido). parent(maya, ido).
parent(yair, maor). parent(maya, maor).

% Parent relations (Fictional extended family)
parent(moshe, yair). parent(rachel, yair).
parent(haim, maya). parent(sara, maya).
parent(moshe, pnina). parent(rachel, pnina).
parent(shlomo, dan). parent(pnina, dan).
parent(yonatan, tamar). parent(michal, tamar).

% 1. Father
father(X, Y) :- male(X), parent(X, Y).

% 2. Mother
mother(X, Y) :- female(X), parent(X, Y).

% 3. Son
son(X, Y) :- male(X), parent(Y, X).

% 4. Daughter
daughter(X, Y) :- female(X), parent(Y, X).

% 5. Grandfather
grandfather(X, Y) :- father(X, Z), parent(Z, Y).

% 6. Grandmother
grandmother(X, Y) :- mother(X, Z), parent(Z, Y).

% 7. Grandson
grandson(X, Y) :- son(X, Z), parent(Y, Z).

% 8. Granddaughter
granddaughter(X, Y) :- daughter(X, Z), parent(Y, Z).

% 9. Sibling
sibling(X, Y) :- father(F, X), father(F, Y), mother(M, X), mother(M, Y), X \= Y.

% 10. Uncle with no blood relation (Husband of parent's sister)
uncle_no_blood(X, Y) :- married(X, Aunt), sibling(Aunt, Parent), parent(Parent, Y).

% 11. Ben-Doda (Male cousin, son of an aunt)
ben_doda(X, Y) :- male(X), mother(Aunt, X), sibling(Aunt, Parent), parent(Parent, Y).

% 12. Brother-in-law (Gis) - Can be husband of sibling OR brother of spouse
brother_in_law(X, Y) :- married(X, Sibling), sibling(Sibling, Y).
brother_in_law(X, Y) :- male(X), sibling(X, Spouse), married(Spouse, Y).
brother_in_law(X, Y) :- male(X), sibling(X, Spouse), married(Y, Spouse).

% 13. Niece
niece(X, Y) :- female(X), parent(Parent, X), sibling(Parent, Y).

% 14. Second cousin (Parents of X and Y are first cousins)
first_cousin(A, B) :- parent(ParentA, A), parent(ParentB, B), sibling(ParentA, ParentB).
second_cousin(X, Y) :- parent(ParentX, X), parent(ParentY, Y), first_cousin(ParentX, ParentY).