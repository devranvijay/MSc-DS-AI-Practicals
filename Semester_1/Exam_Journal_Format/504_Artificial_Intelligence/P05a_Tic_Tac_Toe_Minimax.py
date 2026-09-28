# ------------------------------------------------------
# Practical No: 5 (a)
# Aim: To implement a Tic-Tac-Toe game playing agent using the
#      Minimax algorithm in Python.
# ------------------------------------------------------

# Theory:
# Minimax is a decision-making algorithm used in two player games.
# The computer (maximizer) tries to maximize its score while assuming
# the human (minimizer) always plays the best possible move. By
# exploring all possible future moves, the computer can choose the
# move that leads to the best guaranteed outcome, making it unbeatable
# in Tic-Tac-Toe.

# Algorithm:
# 1. Start
# 2. If the board has a winner or is full, return the score of that state
# 3. If it is the computer's turn, try every empty cell and pick the
#    move with the maximum score
# 4. If it is the human's turn, try every empty cell and pick the move
#    with the minimum score
# 5. Repeat for every possible move to find the best move for the computer
# 6. Stop

# Python Program:

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def check_winner(b):
    win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]
    for line in win_lines:
        x, y, z = line
        if b[x] == b[y] == b[z] and b[x] != "_":
            return b[x]
    return None


def minimax(b, is_max):
    winner = check_winner(b)
    if winner == "O":
        return 10
    if winner == "X":
        return -10
    if "_" not in b:
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == "_":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = "_"
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == "_":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = "_"
        return best


# Setting up a sample mid-game board to find the computer's best move
board = ["X", "O", "X",
         "X", "O", "_",
         "_", "_", "O"]

print("Current board:")
print(board[0:3])
print(board[3:6])
print(board[6:9])

best_score = -1000
best_move = -1
for i in range(9):
    if board[i] == "_":
        board[i] = "O"
        score = minimax(board, False)
        board[i] = "_"
        if score > best_score:
            best_score = score
            best_move = i

print("Best move for computer (O) is at position:", best_move)

# Sample Input / Output:
# Current board:
# ['X', 'O', 'X']
# ['X', 'O', '_']
# ['_', '_', 'O']
# Best move for computer (O) is at position: 7

# Result:
# The program to implement Tic-Tac-Toe using the Minimax algorithm
# was executed successfully and the output was verified.

# Viva Questions:
# 1. Why is the computer called the maximizer and the human the minimizer?
# 2. What score is returned when the computer (O) wins?
# 3. What score is returned when the game is a draw?
# 4. Can the Minimax agent in Tic-Tac-Toe ever lose? Why?
# 5. What is the base case in this recursive Minimax function?
