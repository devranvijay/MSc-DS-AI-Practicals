# Practical 06 — Number Puzzle (8-Puzzle)

**Subject:** 504 – Artificial Intelligence
**File:** `number_puzzle_8_puzzle.py`

## Aim
To solve the classic 8-Puzzle sliding-tile problem using A* search
with the Manhattan Distance heuristic.

## Theory
The 8-puzzle consists of a 3x3 grid with 8 numbered tiles and one
blank space; the goal is to reach a target arrangement by repeatedly
sliding a tile adjacent to the blank into the blank space. Each
arrangement is a **state**, and each slide is an **action** connecting
two states, turning the puzzle into a graph-search problem. The
**Manhattan Distance heuristic** sums, for every tile, the number of
grid rows and columns it is away from its goal position — this is
admissible because at minimum a tile must move that many steps.
Solvability is determined by inversion count parity: a configuration
is solvable if and only if its number of inversions is even.

## How to Run
```bash
python number_puzzle_8_puzzle.py
```

## Viva Questions & Answers
1. **Q: What does "state space" mean in the context of the 8-puzzle?**
   A: The set of all possible tile arrangements, connected by edges
   representing valid single-tile slides.
2. **Q: Why is the Manhattan Distance heuristic admissible?**
   A: Because each tile must move at least as many steps as its
   Manhattan distance to reach its goal position — the heuristic never
   overestimates the true remaining cost.
3. **Q: How do you determine whether an 8-puzzle configuration is solvable?**
   A: Count inversions among the tiles (ignoring the blank); the
   puzzle is solvable if and only if this count is even.
4. **Q: Why not use plain BFS instead of A* for the 8-puzzle?**
   A: BFS still finds the optimal solution but explores far more
   states since it has no guidance toward the goal; A* uses the
   heuristic to explore promising states first, dramatically reducing
   the search space in practice.
5. **Q: What is the maximum branching factor at any state of the 8-puzzle?**
   A: 4 (the blank can move up, down, left, or right), fewer at edges/corners.

## Real-World Relevance
The 8-puzzle is a standard AI benchmark for evaluating heuristic
search; the same techniques scale to real path-planning and
robot-motion problems.
