# Practical 01 — DFS & BFS

**Subject:** 504 – Artificial Intelligence
**File:** `dfs_bfs.py`

## Aim
To implement Depth-First Search (DFS) and Breadth-First Search (BFS)
on a graph represented as an adjacency list, and compare their
traversal order.

## Theory
Both DFS and BFS are **uninformed (blind) search** strategies — they
explore a graph without any domain-specific heuristic.
- **DFS** explores as far as possible along each branch before
  backtracking, using a stack (LIFO) — either an explicit stack or the
  call stack via recursion.
- **BFS** explores all neighbors at the current depth before moving to
  nodes at the next depth level, using a queue (FIFO). BFS guarantees
  the shortest path in an unweighted graph.

| Property        | DFS                     | BFS                        |
|------------------|-------------------------|-----------------------------|
| Data structure   | Stack                   | Queue                      |
| Space complexity | O(depth of tree)        | O(branching factor ^ depth)|
| Shortest path?   | Not guaranteed          | Guaranteed (unweighted)    |
| Time complexity  | O(V + E)                | O(V + E)                   |

## How to Run
```bash
python dfs_bfs.py
```

## Sample Output
```
DFS traversal (iterative)  from 'A': ['A', 'B', 'D', 'E', 'G', 'C', 'F']
BFS traversal              from 'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

## Viva Questions & Answers
1. **Q: Why does BFS guarantee the shortest path in an unweighted graph?**
   A: Because it explores nodes level by level — all nodes at
   distance `d` are visited before any node at distance `d+1`.
2. **Q: What data structure is central to each algorithm?**
   A: DFS uses a stack (LIFO); BFS uses a queue (FIFO).
3. **Q: What is the time and space complexity of DFS/BFS?**
   A: Time: O(V + E) for both, where V = vertices, E = edges. Space:
   DFS is O(depth); BFS is O(max width of the graph).
4. **Q: Can DFS get stuck in an infinite loop? How is this avoided?**
   A: Yes, in a graph with cycles — avoided by maintaining a `visited`
   (seen) set so nodes are not revisited.
5. **Q: Give one real-world application each of DFS and BFS.**
   A: DFS: solving mazes / topological sorting; BFS: finding the
   shortest number of hops in a social network / GPS shortest route on
   an unweighted map.

## Real-World Relevance
DFS/BFS form the foundation of pathfinding, web crawlers, social
network analysis, and puzzle-solving AI agents.
