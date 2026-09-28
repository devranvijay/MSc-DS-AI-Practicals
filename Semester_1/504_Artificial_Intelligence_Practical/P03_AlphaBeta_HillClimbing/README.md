# Practical 03 — Alpha-Beta Pruning & Hill Climbing

**Subject:** 504 – Artificial Intelligence
**Files:** `alpha_beta_pruning.py`, `hill_climbing.py`

## Aim
(a) To implement Minimax with Alpha-Beta pruning on a game tree and
demonstrate the reduction in nodes evaluated.
(b) To implement Hill Climbing search to find a local maximum of a
function, and observe its tendency to get stuck.

## Theory
**Alpha-Beta Pruning** is an optimization of the Minimax algorithm used
in two-player adversarial games. It maintains two bounds — `alpha`
(best value the maximizer can guarantee so far) and `beta` (best value
the minimizer can guarantee so far) — and **prunes** (skips) any
branch that cannot possibly influence the final decision, without
changing the result Minimax would have produced.

**Hill Climbing** is a local-search optimization technique: starting
from an initial state, it repeatedly moves to the best neighboring
state, stopping when no neighbor improves further. It is simple and
memory-efficient but can get stuck at a **local maximum**, on a
**plateau**, or at a **ridge**, missing the global optimum.

## How to Run
```bash
python alpha_beta_pruning.py
python hill_climbing.py
```

## Viva Questions & Answers
1. **Q: What is the key idea behind Alpha-Beta pruning?**
   A: If a branch is found that is already worse than a previously
   examined option for either player, it can be pruned because a
   rational opponent would never allow that branch to be reached.
2. **Q: Does Alpha-Beta pruning change the final Minimax result?**
   A: No — it produces exactly the same optimal decision as plain
   Minimax, just faster (fewer nodes evaluated).
3. **Q: What is the best-case time complexity improvement from Alpha-Beta pruning?**
   A: With optimal move ordering, Alpha-Beta reduces the effective
   branching factor from `b` to roughly `sqrt(b)`, i.e. from O(b^d) to O(b^(d/2)).
4. **Q: What are the three main failure modes of Hill Climbing?**
   A: Local maxima (a peak lower than the global maximum), plateaus
   (flat regions with no improving neighbor), and ridges (a series of
   local maxima that are difficult to navigate with simple moves).
5. **Q: How can Hill Climbing's local-optimum problem be mitigated?**
   A: Random restarts (retry from multiple starting points), simulated
   annealing (allow occasional worse moves), or using a more informed
   search strategy.

## Real-World Relevance
Alpha-Beta pruning powers real chess/checkers/game-playing engines;
Hill Climbing (and its descendants like simulated annealing) are used
in scheduling, route optimization, and neural-network hyperparameter tuning.
