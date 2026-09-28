# ------------------------------------------------------
# Practical No: 3 (a)
# Aim: To implement the Minimax algorithm with Alpha-Beta pruning
#      in Python.
# ------------------------------------------------------

# Theory:
# Minimax is used in two player games to choose the best move,
# assuming the opponent also plays optimally. Alpha-Beta pruning is
# an optimization of Minimax that skips (prunes) branches of the game
# tree that cannot influence the final decision, thereby reducing the
# number of nodes evaluated.

# Algorithm:
# 1. Start
# 2. If the current depth is the maximum depth, return the leaf value
# 3. If it is the maximizer's turn, find the maximum value among children
#    and update alpha; stop early if beta <= alpha
# 4. If it is the minimizer's turn, find the minimum value among children
#    and update beta; stop early if beta <= alpha
# 5. Return the best value found
# 6. Stop

# Python Program:

leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]


def minimax(depth, node_index, is_max, alpha, beta):
    if depth == 3:
        return leaf_values[node_index]

    if is_max:
        best = -1000
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


result = minimax(0, 0, True, -1000, 1000)
print("Leaf values of game tree:", leaf_values)
print("Optimal value for the maximizer =", result)

# Sample Input / Output:
# Leaf values of game tree: [3, 5, 6, 9, 1, 2, 0, -1]
# Optimal value for the maximizer = 5

# Result:
# The program to implement Minimax with Alpha-Beta pruning was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is the Minimax algorithm used for?
# 2. What do alpha and beta represent in Alpha-Beta pruning?
# 3. Does Alpha-Beta pruning change the final result of Minimax?
# 4. When does pruning (cutting a branch) occur?
# 5. What is the advantage of Alpha-Beta pruning over plain Minimax?
