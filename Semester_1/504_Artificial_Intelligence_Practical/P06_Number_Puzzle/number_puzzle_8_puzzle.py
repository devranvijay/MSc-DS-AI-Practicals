"""
Practical 06: Number Puzzle (8-Puzzle) using A* Search
Subject : 504 - Artificial Intelligence
Aim     : To solve the classic 8-Puzzle (sliding tile puzzle) using A*
          search with the Manhattan Distance heuristic.
"""

import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 represents the blank tile.
BOARD_SIZE = 3


def get_blank_position(state: tuple) -> int:
    """Return the index of the blank tile (0) within the flat state tuple."""
    return state.index(0)


def manhattan_distance_heuristic(state: tuple) -> int:
    """
    Compute the sum of Manhattan distances of every tile from its goal
    position. This heuristic is admissible (never overestimates the true
    number of moves needed).
    """
    total_distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(index, BOARD_SIZE)
        goal_index = GOAL_STATE.index(tile)
        goal_row, goal_col = divmod(goal_index, BOARD_SIZE)

        total_distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return total_distance


def get_possible_moves(state: tuple) -> list:
    """Return all states reachable by sliding a tile into the blank space."""
    blank_index = get_blank_position(state)
    blank_row, blank_col = divmod(blank_index, BOARD_SIZE)

    moves = []
    directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    for row_delta, col_delta, move_name in directions:
        new_row, new_col = blank_row + row_delta, blank_col + col_delta

        if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
            new_index = new_row * BOARD_SIZE + new_col
            new_state = list(state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            moves.append((tuple(new_state), move_name))

    return moves


def solve_8_puzzle(start_state: tuple) -> list:
    """
    Solve the 8-puzzle using A* search with the Manhattan Distance heuristic.

    Returns:
        A list of (state, move_description) tuples from start to goal,
        or an empty list if the puzzle is unsolvable.
    """
    counter = 0  # Tie-breaker so tuples with equal priority compare safely.
    frontier = [(manhattan_distance_heuristic(start_state), counter, start_state, 0, [])]
    best_cost_seen = {start_state: 0}

    while frontier:
        _, _, current_state, cost_so_far, path_so_far = heapq.heappop(frontier)

        if current_state == GOAL_STATE:
            return path_so_far

        for next_state, move_name in get_possible_moves(current_state):
            new_cost = cost_so_far + 1

            if next_state not in best_cost_seen or new_cost < best_cost_seen[next_state]:
                best_cost_seen[next_state] = new_cost
                priority = new_cost + manhattan_distance_heuristic(next_state)
                counter += 1
                heapq.heappush(
                    frontier,
                    (priority, counter, next_state, new_cost, path_so_far + [(next_state, move_name)]),
                )

    return []


def is_solvable(state: tuple) -> bool:
    """
    Check solvability of an 8-puzzle configuration by counting inversions.
    A configuration is solvable if and only if the number of inversions
    (ignoring the blank) is even.
    """
    tiles = [tile for tile in state if tile != 0]
    inversions = sum(
        1
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
        if tiles[i] > tiles[j]
    )
    return inversions % 2 == 0


def print_state(state: tuple) -> None:
    """Pretty-print a 3x3 puzzle state, showing the blank as an empty cell."""
    for row in range(BOARD_SIZE):
        cells = state[row * BOARD_SIZE:(row + 1) * BOARD_SIZE]
        print("  " + " ".join(str(tile) if tile != 0 else "_" for tile in cells))


def main() -> None:
    """Entry point that drives the 8-puzzle A* demonstration."""
    print("=" * 60)
    print("PRACTICAL 06 : NUMBER PUZZLE (8-PUZZLE) USING A* SEARCH")
    print("=" * 60)

    start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    print("\nStart state:")
    print_state(start_state)
    print("\nGoal state:")
    print_state(GOAL_STATE)

    if not is_solvable(start_state):
        print("\nThis configuration is NOT solvable.")
        return

    solution_path = solve_8_puzzle(start_state)

    print(f"\nSolution found in {len(solution_path)} moves:")
    for step_number, (state, move_name) in enumerate(solution_path, start=1):
        print(f"\nStep {step_number}: slide blank {move_name}")
        print_state(state)

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
