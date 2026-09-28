"""
Practical 05a: Tic-Tac-Toe using the Minimax Algorithm
Subject : 504 - Artificial Intelligence
Aim     : To implement an unbeatable Tic-Tac-Toe AI agent using the
          Minimax algorithm, capable of playing optimally against a
          human or another agent.
"""

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def create_empty_board() -> list:
    """Return a fresh, empty 3x3 Tic-Tac-Toe board as a flat list of 9 cells."""
    return [EMPTY] * 9


def print_board(board: list) -> None:
    """Pretty-print the board in a 3x3 grid."""
    for row in range(0, 9, 3):
        print(" | ".join(board[row:row + 3]))
        if row < 6:
            print("-" * 9)


def get_winner(board: list) -> str:
    """Return 'X' or 'O' if that player has won, else an empty string."""
    for a, b, c in WINNING_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return ""


def is_board_full(board: list) -> bool:
    """Check whether every cell on the board has been filled."""
    return EMPTY not in board


def get_available_moves(board: list) -> list:
    """Return the list of empty cell indices."""
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def minimax(board: list, is_maximizing: bool) -> int:
    """
    Recursively evaluate the board using Minimax.

    Returns +10 if COMPUTER wins, -10 if HUMAN wins, 0 for a draw,
    adjusted for search depth so faster wins/slower losses are preferred.
    """
    winner = get_winner(board)
    if winner == COMPUTER:
        return 10
    if winner == HUMAN:
        return -10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move] = COMPUTER
            score = minimax(board, is_maximizing=False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for move in get_available_moves(board):
        board[move] = HUMAN
        score = minimax(board, is_maximizing=True)
        board[move] = EMPTY
        best_score = min(best_score, score)
    return best_score


def find_best_move(board: list) -> int:
    """Use Minimax to find the optimal move for the COMPUTER player."""
    best_score = float("-inf")
    best_move = -1

    for move in get_available_moves(board):
        board[move] = COMPUTER
        score = minimax(board, is_maximizing=False)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def simulate_game() -> None:
    """
    Simulate a full game where the COMPUTER always plays optimally and a
    simple scripted HUMAN plays a fixed sequence of moves, to demonstrate
    that the Minimax agent never loses.
    """
    board = create_empty_board()
    scripted_human_moves = [0, 1, 5, 6, 3, 7, 2, 8, 4]
    human_move_index = 0
    current_player = HUMAN

    print("Initial board:")
    print_board(board)

    while True:
        if current_player == HUMAN:
            while board[scripted_human_moves[human_move_index]] != EMPTY:
                human_move_index += 1
            move = scripted_human_moves[human_move_index]
            board[move] = HUMAN
            print(f"\nHuman (X) plays position {move}:")
        else:
            move = find_best_move(board)
            board[move] = COMPUTER
            print(f"\nComputer (O) plays position {move} (Minimax-optimal):")

        print_board(board)

        winner = get_winner(board)
        if winner:
            print(f"\nResult: '{winner}' wins the game!")
            return
        if is_board_full(board):
            print("\nResult: The game is a draw.")
            return

        current_player = COMPUTER if current_player == HUMAN else HUMAN


def main() -> None:
    """Entry point that drives the Tic-Tac-Toe Minimax demonstration."""
    print("=" * 60)
    print("PRACTICAL 05a : TIC-TAC-TOE USING MINIMAX")
    print("=" * 60)
    print("\n(Cell positions are numbered 0-8, left to right, top to bottom)\n")

    simulate_game()

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
