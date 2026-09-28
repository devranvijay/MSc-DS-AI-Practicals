"""
Practical 04b: Water Jug Problem
Subject : 504 - Artificial Intelligence
Aim     : To solve the classic Water Jug problem (measure exactly a
          target amount of water using two jugs of given capacities)
          using Breadth-First Search over the state space.
"""

from collections import deque


def get_possible_moves(state: tuple, capacity_a: int, capacity_b: int) -> list:
    """
    Given the current state (amount in jug A, amount in jug B), return
    all states reachable via one valid jug operation: fill, empty, or pour.
    """
    amount_a, amount_b = state
    possible_next_states = []

    # Fill jug A or jug B completely.
    possible_next_states.append((capacity_a, amount_b))
    possible_next_states.append((amount_a, capacity_b))

    # Empty jug A or jug B completely.
    possible_next_states.append((0, amount_b))
    possible_next_states.append((amount_a, 0))

    # Pour from A into B, until A is empty or B is full.
    pour_amount = min(amount_a, capacity_b - amount_b)
    possible_next_states.append((amount_a - pour_amount, amount_b + pour_amount))

    # Pour from B into A, until B is empty or A is full.
    pour_amount = min(amount_b, capacity_a - amount_a)
    possible_next_states.append((amount_a + pour_amount, amount_b - pour_amount))

    return possible_next_states


def solve_water_jug(capacity_a: int, capacity_b: int, target_amount: int) -> list:
    """
    Solve the Water Jug problem using BFS over the state space, guaranteeing
    the shortest sequence of operations.

    Args:
        capacity_a: Capacity of jug A.
        capacity_b: Capacity of jug B.
        target_amount: The exact amount of water we want in either jug.

    Returns:
        A list of states (tuples) from the initial state to a goal state,
        or an empty list if the target is unreachable.
    """
    initial_state = (0, 0)
    if target_amount in (0,):
        return [initial_state]

    frontier = deque([initial_state])
    came_from = {initial_state: None}

    while frontier:
        current_state = frontier.popleft()
        amount_a, amount_b = current_state

        if amount_a == target_amount or amount_b == target_amount:
            return reconstruct_path(came_from, current_state)

        for next_state in get_possible_moves(current_state, capacity_a, capacity_b):
            if next_state not in came_from:
                came_from[next_state] = current_state
                frontier.append(next_state)

    return []


def reconstruct_path(came_from: dict, goal_state: tuple) -> list:
    """Rebuild the path of states from the initial state to the goal state."""
    path = []
    state = goal_state
    while state is not None:
        path.append(state)
        state = came_from[state]
    path.reverse()
    return path


def main() -> None:
    """Entry point that drives the Water Jug problem demonstration."""
    print("=" * 60)
    print("PRACTICAL 04b : WATER JUG PROBLEM")
    print("=" * 60)

    capacity_a, capacity_b, target = 4, 3, 2
    print(f"\nJug A capacity : {capacity_a} litres")
    print(f"Jug B capacity : {capacity_b} litres")
    print(f"Target amount  : {target} litres (in either jug)")

    solution_path = solve_water_jug(capacity_a, capacity_b, target)

    if solution_path:
        print(f"\nSolution found in {len(solution_path) - 1} steps:")
        print(f"{'Step':>5} | {'Jug A':>6} | {'Jug B':>6}")
        print("-" * 22)
        for step_number, (amount_a, amount_b) in enumerate(solution_path):
            print(f"{step_number:>5} | {amount_a:>6} | {amount_b:>6}")
    else:
        print("\nNo solution exists for this combination of capacities and target.")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
