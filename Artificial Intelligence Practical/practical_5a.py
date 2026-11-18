# ===== 5a. Tic-Tac-Toe using Min-Max Algorithm =====
board = [" "] * 9
def display():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
def winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None
def minimax(maximizing):
    win = winner()
    if win == "O":
        return 1
    if win == "X":
        return -1
    if " " not in board:
        return 0
    if maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
def best_move():
    best = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best:
                best = score
                move = i
    return move
while True:
    display()
    try:
        pos = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue
    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue
    board[pos] = "X"
    if winner() == "X":
        display()
        print("You win!")
        break
    if " " not in board:
        display()
        print("Draw!")
        break
    board[best_move()] = "O"
    if winner() == "O":
        display()
        print("Computer wins!")
        break
    if " " not in board:
        display()
        print("Draw!")
        break
