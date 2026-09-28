# Practical 02 — Relational & Logical Operators

**Subject:** 502 – Essential Technologies for Data Science
**File:** `relational_logical_operators.py`

## Aim
To demonstrate relational operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
and logical operators (`and`, `or`, `not`), including short-circuit
evaluation, using a real-world voter-eligibility example.

## Theory
Relational operators compare two values and always evaluate to a
Boolean (`True`/`False`). Logical operators combine Boolean
expressions: `and` is `True` only if both operands are `True`, `or` is
`True` if at least one operand is `True`, and `not` inverts a Boolean
value. Python's `and`/`or` are **short-circuiting** — evaluation stops
as soon as the outcome is already certain, which matters for both
performance and for avoiding errors (e.g. `x != 0 and 10/x > 1`).

## How to Run
```bash
python relational_logical_operators.py
```

## Sample Output
```
Age = 20, Has ID card = True
--------------------------------------------------
is_adult (age >= 18)               : True
can_vote (is_adult AND has_id_card) : True
can_apply_for_id (is_adult OR id)   : True
id_missing (NOT has_id_card)        : False
```

## Viva Questions & Answers
1. **Q: What is the difference between `=` and `==` in Python?**
   A: `=` is the assignment operator; `==` is the equality (relational)
   comparison operator.
2. **Q: What does short-circuit evaluation mean?**
   A: In `A and B`, if `A` is `False`, `B` is never evaluated because
   the result is already `False`; similarly, in `A or B`, if `A` is
   `True`, `B` is skipped.
3. **Q: What is the output of `not (5 > 3)`?**
   A: `False`, because `5 > 3` is `True` and `not` inverts it.
4. **Q: Can relational operators be chained in Python?**
   A: Yes — `1 < x < 10` is valid and equivalent to
   `1 < x and x < 10`.
5. **Q: Why is short-circuit evaluation useful in real code?**
   A: It prevents errors, e.g. checking `x != 0 and (10 / x) > 2`
   safely avoids a divide-by-zero when `x` is 0.

## Real-World Relevance
Relational and logical operators drive every conditional/filtering
operation in data pipelines — from `pandas` boolean masking
(`df[df["age"] > 18]`) to validation rules in ETL scripts.
