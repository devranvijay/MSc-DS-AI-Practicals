# Practical 10 — Family Tree using Prolog Predicates

**Subject:** 504 – Artificial Intelligence
**Files:** `family_tree.pl` (Prolog source), `family_tree_simulation.py`
(Python simulation of the same logic, so the practical can be
demonstrated without a separate Prolog installation)

## Aim
To represent a family tree using Prolog facts (`parent`, `male`,
`female`) and rules (`father`, `mother`, `sibling`, `grandparent`,
`uncle`, `aunt`, `ancestor`) that can be queried to derive family
relationships.

## Theory
Prolog is a **logic programming language** built directly on
predicate logic. A Prolog program consists of:
- **Facts**: unconditionally true statements, e.g. `parent(dinesh, ramesh).`
- **Rules**: conditional statements of the form
  `head :- body1, body2, ...` (read "head is true IF body1 AND
  body2 ... are true").
- **Queries**: questions posed to the Prolog engine, e.g.
  `?- father(ramesh, aditi).`, answered via **backward chaining** and
  **unification** (Prolog's built-in inference mechanism).

## How to Run

**Option A — with SWI-Prolog installed** (https://www.swi-prolog.org):
```bash
swipl family_tree.pl
?- father(ramesh, aditi).
?- sibling(aditi, arjun).
?- grandfather(dinesh, aditi).
?- ancestor(dinesh, meera).
```

**Option B — pure Python (no external installation needed):**
```bash
python family_tree_simulation.py
```

## Sample Output (Python simulation)
```
father(aditi)            : ['ramesh']
mother(aditi)            : ['kavita']
siblings(aditi)          : {'arjun'}
grandparents(aditi)      : {'dinesh', 'sunita'}
uncles/aunts(aditi)      : {'suresh'}
ancestors(aditi)         : {'ramesh', 'kavita', 'dinesh', 'sunita'}
```

## Viva Questions & Answers
1. **Q: What is unification in Prolog?**
   A: The process of matching a query against facts/rule heads by
   finding a consistent substitution of variables that makes them
   identical — Prolog's core pattern-matching mechanism.
2. **Q: What is the difference between a fact and a rule in Prolog?**
   A: A fact is unconditionally true (e.g. `parent(dinesh, ramesh).`);
   a rule is conditionally true, derived from other facts/rules via a
   body of conditions (e.g. `father(F, C) :- parent(F, C), male(F).`).
3. **Q: How does Prolog answer a query like `?- sibling(aditi, arjun).`?**
   A: It uses backward chaining — it tries to prove the goal by
   matching it against rule heads, recursively proving each condition
   in the rule's body against the known facts.
4. **Q: Why is the `ancestor` rule defined recursively?**
   A: Because "ancestor" can span an arbitrary number of generations;
   the recursive rule reduces the problem to "either a direct parent,
   or a parent of an ancestor," matching however many generations exist.
5. **Q: How would you prevent Prolog from finding a person as their own
   sibling?**
   A: Add the constraint `PersonA \\= PersonB` (not equal) in the
   sibling rule body, as done in `family_tree.pl`.

## Real-World Relevance
Prolog and predicate-logic-based reasoning are used in expert systems,
natural-language understanding, automated theorem proving, and
knowledge-graph query engines.
