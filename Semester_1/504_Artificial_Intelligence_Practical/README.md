# 504 — Artificial Intelligence Practical

**Semester:** I | **University:** University of Mumbai (UoM) | **Practicals:** 10

This subject covers the classical foundations of Artificial
Intelligence: uninformed and informed search, adversarial (game-tree)
search, local search, constraint satisfaction, and formal logic —
implemented from first principles in Python (plus one practical in
native Prolog) rather than via a black-box library, so the underlying
algorithms are fully visible and explainable at viva.

## Practicals in this Subject

| # | Practical | Algorithm(s) / Concepts |
|---|-----------|--------------------------|
| 1 | DFS & BFS | Uninformed graph search |
| 2 | N-Queen & Tower of Hanoi | Backtracking, recursion |
| 3 | Alpha-Beta pruning & Hill Climbing | Adversarial search, local search |
| 4 | A* Search & Water Jug problem | Informed search, state-space search |
| 5 | Tic-Tac-Toe (Minimax) & Shuffle Cards | Game-tree search, randomized algorithms |
| 6 | Number Puzzle (8-Puzzle) | A* search with Manhattan Distance heuristic |
| 7 | Constraint Satisfaction Problem | Backtracking CSP (map coloring) |
| 8 | Associative & Distributive Law | Boolean algebra, set theory |
| 9 | Predicate Logic | First-order logic, forward-chaining inference |
| 10 | Family Tree using Prolog Predicates | Prolog facts/rules, unification |

## Learning Progression

Practicals 1 lays the groundwork with the two fundamental blind-search
strategies. Practicals 2-4 build up backtracking, adversarial pruning,
local search, and heuristic-guided (informed) search. Practical 5
applies game-tree search to a complete playable game. Practical 6
combines several earlier ideas (state-space search + heuristics) into
a harder puzzle. Practicals 7-10 shift from *search* to *logic and
constraint reasoning* — the other major pillar of classical AI,
culminating in an actual Prolog program.

## How to Run Any Practical

```bash
cd P01_DFS_BFS
python dfs_bfs.py
```

Practical 10 additionally includes a real Prolog source file
(`family_tree.pl`) runnable with SWI-Prolog, alongside a pure-Python
simulation of the same logic so the practical can be demonstrated
without any extra installation.

See the repository root `README.md` for the full index and setup
instructions, and each practical's own `README.md` for its aim,
theory, sample output, and viva questions.
