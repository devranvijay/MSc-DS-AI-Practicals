"""
Practical 03b: Hill Climbing Algorithm
Subject : 504 - Artificial Intelligence
Aim     : To implement the Hill Climbing search algorithm to find a
          local maximum of a mathematical function, and observe how it
          can get stuck at a local optimum.
"""

import random


def objective_function(x: float) -> float:
    """
    A multi-modal function with several local maxima, used to test
    Hill Climbing's tendency to get stuck away from the global maximum.
    """
    return -(x ** 2) + 10 * (x % 5 == 0) - 0.5 * (x - 6) ** 2 + 40


def get_neighbors(current_x: float, step_size: float) -> list:
    """Return the two neighboring states reachable by taking one step left/right."""
    return [current_x - step_size, current_x + step_size]


def hill_climbing(start_x: float, step_size: float = 0.5,
                   max_iterations: int = 1000) -> tuple:
    """
    Perform simple (steepest-ascent) Hill Climbing starting from start_x.

    Args:
        start_x: Initial state (starting point on the x-axis).
        step_size: How far each neighboring state is from the current one.
        max_iterations: Safety cap on the number of iterations.

    Returns:
        A tuple (best_x, best_value, iterations_taken).
    """
    current_x = start_x
    current_value = objective_function(current_x)

    for iteration in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_x, step_size)
        neighbor_values = [(neighbor, objective_function(neighbor)) for neighbor in neighbors]

        best_neighbor_x, best_neighbor_value = max(neighbor_values, key=lambda pair: pair[1])

        if best_neighbor_value <= current_value:
            # No neighbor improves on the current state - we are at a
            # local (or global) maximum, so the search stops here.
            return current_x, current_value, iteration

        current_x, current_value = best_neighbor_x, best_neighbor_value

    return current_x, current_value, max_iterations


def main() -> None:
    """Entry point that drives the Hill Climbing demonstration."""
    print("=" * 60)
    print("PRACTICAL 03b : HILL CLIMBING ALGORITHM")
    print("=" * 60)

    random.seed(42)
    starting_points = [-8, -2, 3, 9]

    print("\nSearching for a maximum of the objective function from "
          "several starting points:")
    print(f"{'Start X':>10} | {'Final X':>10} | {'Final Value':>12} | {'Iterations':>10}")
    print("-" * 52)

    for start in starting_points:
        best_x, best_value, iterations = hill_climbing(start_x=start)
        print(f"{start:>10} | {best_x:>10.2f} | {best_value:>12.3f} | {iterations:>10}")

    print("\nObservation: Different starting points can converge to different "
          "local maxima - this is the classic 'foothills' problem of Hill Climbing.")
    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
