# Practical 02 — N-Queen Problem & Tower of Hanoi

**Subject:** 504 – Artificial Intelligence
**Files:** `n_queen_problem.py`, `tower_of_hanoi.py`

## Aim
(a) To place N queens on an N x N chessboard such that no two attack
each other, using backtracking.
(b) To solve the Tower of Hanoi puzzle using recursion and compute the
minimum number of moves required.

## Theory
**N-Queen (Backtracking):** Backtracking incrementally builds a
solution (placing one queen per row) and abandons ("backtracks") a
partial solution as soon as it violates a constraint (same column or
diagonal as a previously placed queen) — far more efficient than
brute-force enumeration of all placements.

**Tower of Hanoi (Recursion):** The classic recursive puzzle: move
`n` disks from a source peg to a destination peg (using an auxiliary
peg), never placing a larger disk on a smaller one. The recursive
insight: to move `n` disks, first move the top `n-1` disks out of the
way, move the largest disk directly, then move the `n-1` disks onto
it. This yields the recurrence `T(n) = 2*T(n-1) + 1`, solved by
`T(n) = 2^n - 1`.

## How to Run
```bash
python n_queen_problem.py
python tower_of_hanoi.py
```

## Sample Output (Tower of Hanoi, n=3)
```
Step  1: Move disk 1 from A -> C
Step  2: Move disk 2 from A -> B
Step  3: Move disk 1 from C -> B
Step  4: Move disk 3 from A -> C
Step  5: Move disk 1 from B -> A
Step  6: Move disk 2 from B -> C
Step  7: Move disk 1 from A -> C
Minimum moves needed: 7 (2^n - 1)
```

## Viva Questions & Answers
1. **Q: What is backtracking and how does it differ from brute force?**
   A: Backtracking builds a solution incrementally and prunes a branch
   the moment a constraint is violated, avoiding wasted exploration
   that brute force would perform.
2. **Q: Why is checking the diagonal condition
   `abs(row1-row2) == abs(col1-col2)` sufficient for the N-Queen problem?**
   A: Two positions lie on the same diagonal if and only if the
   absolute difference in their rows equals the absolute difference in
   their columns.
3. **Q: What is the time complexity of the Tower of Hanoi recursive solution?**
   A: O(2^n), since each call spawns two recursive calls on `n-1` disks.
4. **Q: What is the minimum number of moves for `n` disks in Tower of Hanoi?**
   A: `2^n - 1`.
5. **Q: How many solutions exist for the 8-Queens problem?**
   A: 92 total solutions (12 unique up to symmetry).

## Real-World Relevance
Backtracking search underlies constraint solvers, Sudoku solvers, and
compiler register allocation; recursive divide-and-conquer thinking
(Tower of Hanoi) is foundational to algorithm design broadly.
