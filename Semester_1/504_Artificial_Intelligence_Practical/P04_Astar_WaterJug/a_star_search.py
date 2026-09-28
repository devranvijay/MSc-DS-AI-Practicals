"""
Practical 04a: A* Search Algorithm
Subject : 504 - Artificial Intelligence
Aim     : To implement the A* search algorithm to find the shortest
          path between two nodes in a weighted graph, using a heuristic
          function to guide the search.
"""

import heapq


def build_weighted_graph() -> dict:
    """Build a sample weighted graph as an adjacency list of (neighbor, cost) pairs."""
    return {
        "A": [("B", 4), ("C", 3)],
        "B": [("A", 4), ("D", 5), ("E", 12)],
        "C": [("A", 3), ("D", 7), ("F", 10)],
        "D": [("B", 5), ("C", 7), ("E", 2), ("G", 8)],
        "E": [("B", 12), ("D", 2), ("G", 5)],
        "F": [("C", 10), ("G", 6)],
        "G": [("D", 8), ("E", 5), ("F", 6)],
    }


def build_heuristic_estimates(goal_node: str) -> dict:
    """
    Straight-line-distance-style heuristic estimates to the goal node 'G'.
    These are admissible (never overestimate the true cost) for this graph.
    """
    return {"A": 11, "B": 9, "C": 8, "D": 4, "E": 3, "F": 4, "G": 0}


def a_star_search(graph: dict, start_node: str, goal_node: str, heuristic: dict) -> tuple:
    """
    Find the lowest-cost path from start_node to goal_node using A*.

    Args:
        graph: Weighted adjacency list {node: [(neighbor, cost), ...]}.
        start_node: The starting node.
        goal_node: The target node.
        heuristic: A dict mapping each node to its estimated cost to the goal.

    Returns:
        A tuple (path, total_cost). path is an empty list if no path exists.
    """
    # Priority queue entries: (estimated_total_cost, node, path_so_far, cost_so_far)
    frontier = [(heuristic[start_node], start_node, [start_node], 0)]
    best_cost_to_node = {start_node: 0}

    while frontier:
        _, current_node, path_so_far, cost_so_far = heapq.heappop(frontier)

        if current_node == goal_node:
            return path_so_far, cost_so_far

        for neighbor, edge_cost in graph.get(current_node, []):
            new_cost = cost_so_far + edge_cost

            if neighbor not in best_cost_to_node or new_cost < best_cost_to_node[neighbor]:
                best_cost_to_node[neighbor] = new_cost
                estimated_total = new_cost + heuristic.get(neighbor, 0)
                heapq.heappush(
                    frontier,
                    (estimated_total, neighbor, path_so_far + [neighbor], new_cost),
                )

    return [], float("inf")


def main() -> None:
    """Entry point that drives the A* search demonstration."""
    print("=" * 60)
    print("PRACTICAL 04a : A* SEARCH ALGORITHM")
    print("=" * 60)

    graph = build_weighted_graph()
    heuristic = build_heuristic_estimates(goal_node="G")
    start, goal = "A", "G"

    print(f"\nFinding the shortest path from '{start}' to '{goal}' ...")
    path, total_cost = a_star_search(graph, start, goal, heuristic)

    if path:
        print(f"Shortest path found: {' -> '.join(path)}")
        print(f"Total path cost    : {total_cost}")
    else:
        print("No path found between the given nodes.")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
