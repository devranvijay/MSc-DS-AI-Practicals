# Practical 07 — Constraint Satisfaction Problem (Map Coloring)

**Subject:** 504 – Artificial Intelligence
**File:** `map_coloring_csp.py`

## Aim
To model and solve the Map Coloring problem as a Constraint
Satisfaction Problem (CSP) using backtracking search.

## Theory
A **CSP** is defined by:
- **Variables**: the regions to be colored.
- **Domains**: the set of possible colors for each region.
- **Constraints**: no two adjacent regions may share the same color.

Backtracking search assigns values to variables one at a time,
checking consistency with the constraints after each assignment, and
backtracking (undoing the last assignment) whenever a dead end is
reached. This is a general-purpose technique for any CSP — map
coloring, Sudoku, N-Queens, and scheduling problems all fit this
framework.

## How to Run
```bash
python map_coloring_csp.py
```

## Sample Output
```
A valid coloring was found:
  Western Australia   : Red
  Northern Territory  : Green
  South Australia     : Blue
  Queensland          : Red
  New South Wales     : Green
  Victoria            : Red
  Tasmania            : Red
```

## Viva Questions & Answers
1. **Q: What are the three components that define any CSP?**
   A: Variables, their domains (possible values), and the constraints
   that restrict which combinations of values are valid.
2. **Q: Why does Tasmania not affect the coloring of the mainland regions?**
   A: It has no shared border (no adjacency constraint) with any other
   region, so it can be assigned any available color independently.
3. **Q: What is the minimum number of colors needed to color any planar map?**
   A: Four (the Four Color Theorem) — though this specific problem
   instance can be solved with as few as three.
4. **Q: How could this backtracking search be made more efficient?**
   A: Using heuristics such as Minimum Remaining Values (MRV) to pick
   the most constrained variable next, or Forward Checking / Arc
   Consistency (AC-3) to prune domains early.
5. **Q: Give another real-world problem that can be modeled as a CSP.**
   A: Sudoku, exam timetable scheduling, or register allocation in a
   compiler.

## Real-World Relevance
CSP-solving techniques underpin scheduling systems, Sudoku solvers,
resource allocation, and compiler register allocation.
