"""
Practical 01: Depth-First Search (DFS) and Breadth-First Search (BFS)
Subject : 504 - Artificial Intelligence
Aim     : To implement DFS and BFS graph traversal algorithms on a
          graph represented as an adjacency list, and compare their
          traversal order.
"""

from collections import deque


def build_sample_graph() -> dict:
    """
    Build a sample undirected graph as an adjacency list.

    Graph structure:
            A
           / \\
          B   C
         / \\   \\
        D   E   F
             \\
              G
    """
    return {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C"],
        "G": ["E"],
    }


def depth_first_search(graph: dict, start_node: str) -> list:
    """
    Traverse the graph using DFS (iterative, using an explicit stack).

    Args:
        graph: Adjacency list representation of the graph.
        start_node: The node to start traversal from.

    Returns:
        The list of nodes in the order they were visited.
    """
    visited = []
    visit_stack = [start_node]
    seen = set()

    while visit_stack:
        current_node = visit_stack.pop()
        if current_node in seen:
            continue

        seen.add(current_node)
        visited.append(current_node)

        # Push neighbors in reverse so the leftmost neighbor is explored first.
        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in seen:
                visit_stack.append(neighbor)

    return visited


def depth_first_search_recursive(graph: dict, current_node: str,
                                  seen: set = None, visited: list = None) -> list:
    """Traverse the graph using classic recursive DFS."""
    if seen is None:
        seen = set()
    if visited is None:
        visited = []

    seen.add(current_node)
    visited.append(current_node)

    for neighbor in graph.get(current_node, []):
        if neighbor not in seen:
            depth_first_search_recursive(graph, neighbor, seen, visited)

    return visited


def breadth_first_search(graph: dict, start_node: str) -> list:
    """
    Traverse the graph using BFS (iterative, using a FIFO queue).

    Args:
        graph: Adjacency list representation of the graph.
        start_node: The node to start traversal from.

    Returns:
        The list of nodes in the order they were visited.
    """
    visited = []
    seen = {start_node}
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        visited.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


def main() -> None:
    """Entry point that drives the DFS/BFS demonstration."""
    print("=" * 60)
    print("PRACTICAL 01 : DEPTH-FIRST SEARCH (DFS) AND BREADTH-FIRST SEARCH (BFS)")
    print("=" * 60)

    graph = build_sample_graph()
    print("\nGraph (adjacency list):")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")

    start = "A"
    print(f"\nDFS traversal (iterative)  from '{start}': {depth_first_search(graph, start)}")
    print(f"DFS traversal (recursive)  from '{start}': "
          f"{depth_first_search_recursive(graph, start)}")
    print(f"BFS traversal              from '{start}': {breadth_first_search(graph, start)}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
