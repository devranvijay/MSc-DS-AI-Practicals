# Practical 04 — A* Search & Water Jug Problem

**Subject:** 504 – Artificial Intelligence
**Files:** `a_star_search.py`, `water_jug_problem.py`

## Aim
(a) To implement A* search to find the shortest path in a weighted
graph using an admissible heuristic.
(b) To solve the Water Jug problem via BFS over the state space,
finding the minimum sequence of jug operations.

## Theory
**A\* Search** is an **informed search** algorithm that combines the
actual cost so far (`g(n)`) with a heuristic estimate of the remaining
cost to the goal (`h(n)`), selecting nodes to expand by minimizing
`f(n) = g(n) + h(n)`. If `h(n)` is **admissible** (never overestimates
the true remaining cost), A* is guaranteed to find the optimal path.

**Water Jug Problem** is a classic state-space search problem: given
two jugs of fixed capacity and no markings, measure out an exact
target amount of water using only three operations — fill a jug
completely, empty a jug completely, or pour from one jug into another
until either the source is empty or the destination is full. Modeling
each `(amount_in_A, amount_in_B)` pair as a graph node and each valid
operation as an edge turns this into a standard graph-search problem,
solvable optimally with BFS.

## How to Run
```bash
python a_star_search.py
python water_jug_problem.py
```

## Viva Questions & Answers
1. **Q: What makes a heuristic "admissible"?**
   A: It never overestimates the true cost to reach the goal from a
   given node — this guarantees A* finds an optimal solution.
2. **Q: Why is A* generally more efficient than plain BFS/Dijkstra's algorithm?**
   A: A* uses the heuristic to prioritize expanding nodes that appear
   closer to the goal, reducing the number of nodes explored while
   Dijkstra's expands uniformly by cost alone.
3. **Q: Why does BFS (not DFS) guarantee the minimum number of steps for
   the Water Jug problem?**
   A: BFS explores states level-by-level, so the first time a goal
   state is reached is guaranteed to be via the shortest path (fewest operations).
4. **Q: List the three valid operations in the Water Jug problem.**
   A: Fill a jug completely, empty a jug completely, and pour from one
   jug into the other until one becomes empty or the other becomes full.
5. **Q: What happens to A* if the heuristic is not admissible (overestimates)?**
   A: A* may no longer guarantee the optimal solution, though it can
   still find *a* solution faster.

## Real-World Relevance
A* is the algorithm behind GPS navigation and game-character
pathfinding; state-space search (as in Water Jug) generalizes to
robotics motion planning and puzzle-solving AI.
