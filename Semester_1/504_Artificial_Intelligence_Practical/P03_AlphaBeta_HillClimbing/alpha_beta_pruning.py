"""
Practical 03a: Alpha-Beta Pruning
Subject : 504 - Artificial Intelligence
Aim     : To implement the Minimax algorithm enhanced with Alpha-Beta
          pruning on a small game tree, and demonstrate the reduction
          in the number of nodes evaluated.
"""

# Global counter used purely to demonstrate how many nodes Alpha-Beta
# pruning skips compared to plain Minimax.
nodes_evaluated = 0


def minimax_alpha_beta(depth: int, node_index: int, is_maximizing_player: bool,
                        leaf_values: list, alpha: float, beta: float,
                        max_depth: int) -> int:
    """
    Recursively evaluate a binary game tree using Minimax with Alpha-Beta pruning.

    Args:
        depth: Current depth in the tree (0 = root).
        node_index: Index of the current node among leaf values at this depth.
        is_maximizing_player: True if the current level is a maximizing (MAX) level.
        leaf_values: The terminal (leaf) utility values of the game tree, left to right.
        alpha: Best value the maximizer can currently guarantee.
        beta: Best value the minimizer can currently guarantee.
        max_depth: Depth of the tree (number of edges from root to leaf).

    Returns:
        The minimax value of the current node.
    """
    global nodes_evaluated
    nodes_evaluated += 1

    if depth == max_depth:
        return leaf_values[node_index]

    if is_maximizing_player:
        best_value = float("-inf")
        for child in range(2):
            value = minimax_alpha_beta(
                depth + 1, node_index * 2 + child, False,
                leaf_values, alpha, beta, max_depth,
            )
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cutoff: the minimizer will never allow this branch.
        return best_value

    best_value = float("inf")
    for child in range(2):
        value = minimax_alpha_beta(
            depth + 1, node_index * 2 + child, True,
            leaf_values, alpha, beta, max_depth,
        )
        best_value = min(best_value, value)
        beta = min(beta, best_value)
        if beta <= alpha:
            break  # Alpha cutoff: the maximizer will never allow this branch.
    return best_value


def main() -> None:
    """Entry point that drives the Alpha-Beta pruning demonstration."""
    global nodes_evaluated

    print("=" * 60)
    print("PRACTICAL 03a : ALPHA-BETA PRUNING")
    print("=" * 60)

    # A depth-3 binary game tree with 8 leaf nodes.
    leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
    tree_depth = 3

    print(f"\nGame tree leaf values (left to right): {leaf_values}")

    optimal_value = minimax_alpha_beta(
        depth=0, node_index=0, is_maximizing_player=True,
        leaf_values=leaf_values, alpha=float("-inf"), beta=float("inf"),
        max_depth=tree_depth,
    )

    print(f"\nOptimal value for the MAX player : {optimal_value}")
    print(f"Nodes evaluated with Alpha-Beta  : {nodes_evaluated}")
    print(f"Nodes evaluated by plain Minimax : {2 ** (tree_depth + 1) - 1} "
          "(all nodes, no pruning)")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
