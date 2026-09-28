# Practical 08 — Associative & Distributive Law

**Subject:** 504 – Artificial Intelligence
**File:** `associative_distributive_law.py`

## Aim
To verify the Associative Law and Distributive Law using Boolean
algebra (AND/OR) and Set theory (union/intersection), by exhaustively
testing all combinations of inputs.

## Theory
These are foundational laws of propositional logic and set theory that
underlie AI knowledge representation and rule-based reasoning systems.
- **Associative Law**: `(A . B) . C = A . (B . C)` and
  `(A + B) + C = A + (B + C)` — the grouping of operations does not
  affect the result.
- **Distributive Law**: `A . (B + C) = (A.B) + (A.C)` and
  `A + (B.C) = (A+B).(A+C)` — one operator distributes over another,
  exactly like multiplication distributes over addition in arithmetic.
This script proves both laws hold for **every possible combination**
of Boolean values (a brute-force / exhaustive proof by truth table)
and demonstrates the same identities using concrete Python sets.

## How to Run
```bash
python associative_distributive_law.py
```

## Viva Questions & Answers
1. **Q: Why test "every possible combination" instead of just one example?**
   A: A single example only shows the law holds for that case; to
   prove a logical law universally we must check it holds for all
   possible truth-value assignments (an exhaustive/truth-table proof).
2. **Q: How does the Distributive Law resemble arithmetic?**
   A: AND behaves like multiplication and OR behaves like addition:
   `a * (b + c) = a*b + a*c` mirrors `A AND (B OR C) = (A AND B) OR (A AND C)`.
3. **Q: Why are these laws important in AI knowledge representation?**
   A: They allow logical expressions and rule bases to be
   restructured/simplified (e.g. by a reasoning engine) without
   changing their meaning, which is essential for efficient inference.
4. **Q: What is the set-theory equivalent of Boolean AND and OR?**
   A: AND corresponds to set intersection (`&`); OR corresponds to set
   union (`|`).
5. **Q: Does the Associative Law hold for the Boolean XOR operator?**
   A: Yes — XOR is also associative: `(A XOR B) XOR C == A XOR (B XOR C)`.

## Real-World Relevance
These algebraic identities are used to simplify and optimize logical
circuits, SQL query predicates, and rule-based expert systems.
