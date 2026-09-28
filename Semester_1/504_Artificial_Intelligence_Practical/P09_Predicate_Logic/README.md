# Practical 09 — Predicate Logic

**Subject:** 504 – Artificial Intelligence
**File:** `predicate_logic.py`

## Aim
To represent facts and rules using First-Order Predicate Logic and
implement a forward-chaining inference engine that derives new facts
— the same principle used by Prolog and rule-based expert systems.

## Theory
**Predicate Logic** extends propositional logic with **predicates**
(properties/relations, e.g. `man(X)`), **variables** (`X`), and
**quantifiers** (`for all X`, `there exists X`). A classic example:
```
man(socrates)               (fact)
for all X: man(X) -> mortal(X)   (rule)
--------------------------------------
therefore: mortal(socrates)      (derived by inference)
```
This program implements a small **forward-chaining** inference
engine: it starts from known facts and repeatedly applies rules
(`premises -> conclusion`) to derive new facts, stopping when no rule
can add anything new (a "fixed point"). This is the fundamental
mechanism behind Prolog's reasoning and production-rule expert systems.

## How to Run
```bash
python predicate_logic.py
```

## Viva Questions & Answers
1. **Q: What is the difference between propositional logic and
   predicate logic?**
   A: Propositional logic deals with whole statements (`P`, `Q`) with
   no internal structure; predicate logic introduces predicates,
   variables, and quantifiers, allowing statements like `man(X)` that
   apply to a whole class of entities.
2. **Q: What is forward chaining?**
   A: An inference strategy that starts from known facts and applies
   rules to derive new facts, continuing until no more new facts can
   be derived (data-driven reasoning).
3. **Q: How does forward chaining differ from backward chaining?**
   A: Forward chaining works from facts toward conclusions
   (data-driven); backward chaining starts from a goal/query and works
   backward to see which facts would prove it (goal-driven) — this is
   how Prolog answers queries.
4. **Q: Why does the `forward_chain()` method loop until "no change" occurs?**
   A: Because one derived fact might satisfy the premise of a
   different rule, so the algorithm must keep iterating until a fixed
   point (no new facts) is reached.
5. **Q: What real system uses exactly this kind of reasoning?**
   A: Prolog's inference engine, and rule-based expert systems (e.g.
   medical diagnosis systems, business rule engines).

## Real-World Relevance
Forward/backward chaining inference is the backbone of expert
systems, Prolog programs, and modern rule engines used in
fraud-detection and business-logic automation.
