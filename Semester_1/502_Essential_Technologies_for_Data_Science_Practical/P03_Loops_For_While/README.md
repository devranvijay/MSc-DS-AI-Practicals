# Practical 03 — For & While Loops

**Subject:** 502 – Essential Technologies for Data Science
**File:** `loops_for_while.py`

## Aim
To demonstrate `for` loops, `while` loops, nested loops, and loop
control statements (`break`, `continue`, loop `else`) via multiplication
tables, iterative factorial calculation, and prime-number detection.

## Theory
A `for` loop iterates over a known sequence (e.g. `range()`), while a
`while` loop repeats as long as a condition remains `True` — useful
when the number of iterations isn't known in advance. `break` exits a
loop immediately, `continue` skips to the next iteration, and the
lesser-known `else` clause on a loop runs only if the loop finished
without a `break` (used here to confirm primality).

## How to Run
```bash
python loops_for_while.py
```

## Sample Output
```
Multiplication table of 7 (for loop):
  7 x  1 = 7
  7 x  2 = 14
  ...
Factorial of 6 (while loop) = 720
Prime numbers between 2 and 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

## Viva Questions & Answers
1. **Q: When would you prefer a `while` loop over a `for` loop?**
   A: When the number of iterations is not known beforehand and
   depends on a runtime condition (e.g. reading input until "quit").
2. **Q: What is the purpose of the `else` clause on a `for` loop?**
   A: It executes only if the loop completes fully without
   encountering a `break` — commonly used to confirm a search failed
   to find a match (or, as here, to confirm primality).
3. **Q: What is the time complexity of the prime-checking function?**
   A: O(√n) per number, since divisors are only checked up to the
   square root of `n`.
4. **Q: What is the difference between `break` and `continue`?**
   A: `break` terminates the loop entirely; `continue` skips only the
   current iteration and proceeds to the next one.
5. **Q: How would you convert the iterative factorial to a recursive one?**
   A: `factorial(n) = n * factorial(n-1)` with a base case
   `factorial(0) = 1`.

## Real-World Relevance
Loops are the backbone of every batch-processing task in data science
— iterating over rows of a dataset, epochs in model training, or
records in an ETL pipeline.
