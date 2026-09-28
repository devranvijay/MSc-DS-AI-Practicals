# ------------------------------------------------------
# Practical No: 2 (a)
# Aim: To solve the N-Queen problem using backtracking in Python.
# ------------------------------------------------------

# Theory:
# The N-Queen problem places N queens on an N x N chessboard so that
# no two queens attack each other, that is, no two queens share the
# same row, column or diagonal. Backtracking is used: a queen is
# placed, and if it leads to a conflict later, we go back and try a
# different position.

# Algorithm:
# 1. Start
# 2. Place a queen in a row, one column at a time
# 3. Check if the position is safe (no conflict with earlier queens)
# 4. If safe, move to the next row and repeat
# 5. If not safe, backtrack and try the next column
# 6. When all queens are placed, print the solution
# 7. Stop

# Python Program:

n = 4
board = [-1] * n          # board[row] = column of the queen in that row


def is_safe(row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(row):
    if row == n:
        print(board)
        return True
    for col in range(n):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False


print("Solving", n, "Queens problem")
found = solve(0)
if found:
    print("Solution found. Board (row -> column):", board)
else:
    print("No solution exists")

# Sample Input / Output:
# Solving 4 Queens problem
# Solution found. Board (row -> column): [1, 3, 0, 2]

# Result:
# The program to solve the N-Queen problem using backtracking was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is backtracking?
# 2. Why do two queens on the same diagonal attack each other?
# 3. How many solutions exist for the 8-Queens problem?
# 4. What does board[row] = -1 mean in this program?
# 5. What is the time complexity of the N-Queens backtracking solution?
