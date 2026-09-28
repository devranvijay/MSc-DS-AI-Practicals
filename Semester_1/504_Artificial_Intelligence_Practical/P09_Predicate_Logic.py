# ------------------------------------------------------
# Practical No: 9
# Aim: To represent facts and rules using predicate logic and perform
#      forward chaining inference in Python.
# ------------------------------------------------------

# Theory:
# Predicate logic represents facts using predicates such as
# man(socrates), and rules such as "for all X, if man(X) then
# mortal(X)". Forward chaining starts from known facts and keeps
# applying rules to derive new facts until no more new facts can be
# added. This is the same principle used by Prolog and expert systems.

# Algorithm:
# 1. Start
# 2. Store known facts as a dictionary of entity -> list of known predicates
# 3. Store the rules as (list of required predicates, new predicate)
# 4. Repeat: for every entity, check if all required predicates of a
#    rule are already known; if so, add the new predicate as a fact
# 5. Stop when no new fact is added in a full pass
# 6. Stop

# Python Program:

facts = {
    'socrates': ['man'],
    'plato': ['man'],
    'athena': ['woman'],
}

rules = [
    (['man'], 'mortal'),
    (['woman'], 'mortal'),
    (['mortal', 'man'], 'human'),
]

print("Initial facts:")
for entity in facts:
    for predicate in facts[entity]:
        print(predicate + "(" + entity + ")")

changed = True
while changed:

    changed = False

    for entity in facts:
        for premises, conclusion in rules:

            all_present = all(p in facts[entity] for p in premises)

            if all_present and conclusion not in facts[entity]:
                facts[entity].append(conclusion)
                print("Derived new fact:", conclusion + "(" + entity + ")")
                changed = True

print("\nAll facts after forward chaining:")
for entity in facts:
    for predicate in facts[entity]:
        print(predicate + "(" + entity + ")")

# Sample Input / Output:
# Initial facts:
# man(socrates)
# man(plato)
# woman(athena)
# Derived new fact: mortal(socrates)
# Derived new fact: human(socrates)
# Derived new fact: mortal(plato)
# Derived new fact: human(plato)
# Derived new fact: mortal(athena)
# All facts after forward chaining:
# man(socrates)
# mortal(socrates)
# human(socrates)
# man(plato)
# mortal(plato)
# human(plato)
# woman(athena)
# mortal(athena)

# Result:
# The program to represent predicate logic facts and rules and perform
# forward chaining inference was executed successfully and the output
# was verified.

# Viva Questions:
# 1. What is the difference between a fact and a rule?
# 2. What is forward chaining?
# 3. What is the difference between forward chaining and backward chaining?
# 4. Why does the program keep looping until "changed" becomes False?
# 5. Give one real system that uses this kind of inference.
