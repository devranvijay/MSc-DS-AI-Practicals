% =============================================================
% Practical 10: Family Tree using Prolog Predicates
% Subject : 504 - Artificial Intelligence
% Aim     : To represent a family tree using Prolog facts (parent,
%           male, female) and define rules (father, mother, son,
%           daughter, sibling, grandfather, grandmother, uncle, aunt)
%           that can be queried to derive family relationships.
%
% How to run (requires SWI-Prolog: https://www.swi-prolog.org):
%   swipl family_tree.pl
%   ?- father(ramesh, aditi).
%   ?- sibling(aditi, arjun).
%   ?- grandfather(dinesh, aditi).
% =============================================================

% ---------- FACTS ----------
% parent(Parent, Child).
parent(dinesh, ramesh).
parent(dinesh, suresh).
parent(sunita, ramesh).
parent(sunita, suresh).

parent(ramesh, aditi).
parent(ramesh, arjun).
parent(kavita, aditi).
parent(kavita, arjun).

parent(suresh, meera).
parent(vandana, meera).

% male(Person). / female(Person).
male(dinesh).
male(ramesh).
male(suresh).
male(arjun).

female(sunita).
female(kavita).
female(vandana).
female(aditi).
female(meera).

% ---------- RULES ----------

% father(Father, Child) :- Father is a parent of Child and is male.
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

% mother(Mother, Child) :- Mother is a parent of Child and is female.
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

% son(Son, Parent) :- Son is a child of Parent and is male.
son(Son, Parent) :-
    parent(Parent, Son),
    male(Son).

% daughter(Daughter, Parent) :- Daughter is a child of Parent and is female.
daughter(Daughter, Parent) :-
    parent(Parent, Daughter),
    female(Daughter).

% sibling(PersonA, PersonB) :- they share a parent and are not the same person.
sibling(PersonA, PersonB) :-
    parent(Parent, PersonA),
    parent(Parent, PersonB),
    PersonA \= PersonB.

% brother(Brother, Person) :- Brother is a male sibling of Person.
brother(Brother, Person) :-
    sibling(Brother, Person),
    male(Brother).

% sister(Sister, Person) :- Sister is a female sibling of Person.
sister(Sister, Person) :-
    sibling(Sister, Person),
    female(Sister).

% grandparent(Grandparent, Grandchild) :- via an intermediate parent.
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

% grandfather(Grandfather, Grandchild) :- a male grandparent.
grandfather(Grandfather, Grandchild) :-
    grandparent(Grandfather, Grandchild),
    male(Grandfather).

% grandmother(Grandmother, Grandchild) :- a female grandparent.
grandmother(Grandmother, Grandchild) :-
    grandparent(Grandmother, Grandchild),
    female(Grandmother).

% uncle(Uncle, Person) :- a male sibling of one of Person's parents.
uncle(Uncle, Person) :-
    parent(Parent, Person),
    sibling(Uncle, Parent),
    male(Uncle).

% aunt(Aunt, Person) :- a female sibling of one of Person's parents.
aunt(Aunt, Person) :-
    parent(Parent, Person),
    sibling(Aunt, Parent),
    female(Aunt).

% ancestor(Ancestor, Descendant) :- recursive relationship, any generation back.
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant).
