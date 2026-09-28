# Practical 01 — Arithmetic Operations in Python

**Subject:** 502 – Essential Technologies for Data Science
**File:** `arithmetic_operations.py`

## Aim
To implement and demonstrate all basic arithmetic operators in Python
(`+`, `-`, `*`, `/`, `//`, `%`, `**`), operator precedence (BODMAS), and
augmented assignment operators.

## Theory
Python supports the standard set of arithmetic operators used in
mathematics along with two operators that are particularly useful in
data-science code: floor division (`//`), which returns the integer
quotient, and modulus (`%`), which returns the remainder. Operator
precedence follows BODMAS/PEMDAS — exponentiation is evaluated first,
followed by multiplication/division, and finally addition/subtraction,
with brackets always evaluated first. Augmented assignment operators
(`+=`, `-=`, `*=`, `/=`, `//=`, `**=`) provide a shorthand for
"update a variable using its own value".

## How to Run
```bash
python arithmetic_operations.py
```
The program prompts for two numbers; press Enter without typing anything
to accept the built-in defaults (15 and 4) so the script also runs
non-interactively.

## Sample Output
```
Operands -> a = 15.0, b = 4.0
------------------------------------------------------------
Addition (a + b)           : 19.0
Subtraction (a - b)        : 11.0
Multiplication (a * b)     : 60.0
Exponentiation (a ** b)    : 50625.0
Division (a / b)           : 3.75
Floor Division (a // b)    : 3.0
Modulus (a % b)            : 3.0
```

## Viva Questions & Answers
1. **Q: What is the difference between `/` and `//` in Python?**
   A: `/` always returns a float (true division); `//` returns the
   floor of the quotient (rounded down toward negative infinity).
2. **Q: Why is `%` useful in real programs?**
   A: It gives the remainder of a division, commonly used to check
   divisibility, cycle through indices, or extract digits.
3. **Q: What does BODMAS stand for and why does it matter in code?**
   A: Brackets, Order (powers), Division/Multiplication,
   Addition/Subtraction — it defines the order Python evaluates a
   compound expression, which is essential to avoid logical bugs.
4. **Q: What is an augmented assignment operator? Give an example.**
   A: A shorthand that combines an operation with assignment, e.g.
   `x += 5` is equivalent to `x = x + 5`.
5. **Q: What happens if you divide by zero in Python?**
   A: `/` and `//` raise a `ZeroDivisionError`; the program should
   guard against this with a conditional check or `try/except`.

## Real-World Relevance
Arithmetic operators are the foundation of every numerical computation
in data science — from computing averages and normalizing features to
implementing custom loss functions.
