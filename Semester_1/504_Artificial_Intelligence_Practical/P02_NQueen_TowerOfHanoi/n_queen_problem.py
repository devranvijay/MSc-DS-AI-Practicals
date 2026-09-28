"""
Practical 02a: N-Queen Problem
Subject : 504 - Artificial Intelligence
Aim     : To place N queens on an N x N chessboard such that no two
          queens attack each other, using backtracking.
"""


def is_safe_position(board: list, row: int, col: int, board_size: int) -> bool:
    """
    Check whether placing a queen at (row, col) is safe, i.e. no other
    queen already placed attacks this position via row, or either diagonal.

    Note: Columns are checked only for rows above the current row,
    since we place one queen per row, working top to bottom.
    """
    for previous_row in range(row):
        previous_col = board[previous_row]

        same_column = previous_col == col
        same_diagonal = abs(previous_col - col) == abs(previous_row - row)

        if same_column or same_diagonal:
            return False

    return True


def solve_n_queens(board_size: int) -> list:
    """
    Solve the N-Queen problem using backtracking.

    Args:
        board_size: The size of the board (N) and number of queens.

    Returns:
        A list of all valid solutions; each solution is a list where
        the index is the row and the value is the column of the queen.
    """
    all_solutions = []
    board = [-1] * board_size

    def place_queen(row: int) -> None:
        if row == board_size:
            all_solutions.append(board.copy())
            return

        for col in range(board_size):
            if is_safe_position(board, row, col, board_size):
                board[row] = col
                place_queen(row + 1)
                board[row] = -1  # backtrack

    place_queen(0)
    return all_solutions


def print_board(solution: list, board_size: int) -> None:
    """Pretty-print a single N-Queen solution as a chessboard grid."""
    for row in range(board_size):
        line = ["Q" if solution[row] == col else "." for col in range(board_size)]
        print("  " + " ".join(line))


def main() -> None:
    """Entry point that drives the N-Queen demonstration."""
    print("=" * 60)
    print("PRACTICAL 02a : N-QUEEN PROBLEM (BACKTRACKING)")
    print("=" * 60)

    board_size = 6
    solutions = solve_n_queens(board_size)

    print(f"\nBoard size          : {board_size} x {board_size}")
    print(f"Total solutions found: {len(solutions)}")

    if solutions:
        print("\nFirst solution:")
        print_board(solutions[0], board_size)

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
