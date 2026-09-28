% ------------------------------------------------------
% Practical No: 10
% Aim: To represent a family tree using Prolog predicates and query
%      family relationships.
% ------------------------------------------------------

% Theory:
% Prolog is a logic programming language based on facts and rules.
% Facts state basic relationships (like parent(dinesh, ramesh)).
% Rules define new relationships using existing facts (like father,
% mother, sibling). Prolog answers questions (queries) by matching
% them against these facts and rules.

% Algorithm:
% 1. Start
% 2. Declare parent facts and male/female facts
% 3. Define rules for father, mother, sibling and grandparent using
%    the parent facts
% 4. Run queries such as father(X, aditi) to test the rules
% 5. Stop

% Python Program (Prolog Facts and Rules):

parent(dinesh, ramesh).
parent(sunita, ramesh).
parent(ramesh, aditi).
parent(kavita, aditi).
parent(ramesh, arjun).
parent(kavita, arjun).

male(dinesh).
male(ramesh).
male(arjun).
female(sunita).
female(kavita).
female(aditi).

father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(G, C) :- parent(G, P), parent(P, C).

% Sample Input / Output:
% ?- father(ramesh, aditi).
% true.
% ?- sibling(aditi, arjun).
% true.
% ?- grandparent(dinesh, aditi).
% true.

% Result:
% The Prolog program to represent a family tree and query
% relationships was executed successfully in SWI-Prolog and the
% output was verified.

% Viva Questions:
% 1. What is a fact in Prolog? Give an example.
% 2. What is a rule in Prolog?
% 3. How does Prolog find the answer to a query?
% 4. What does the operator \= mean in the sibling rule?
% 5. How would you define a "grandmother" rule using grandparent?
