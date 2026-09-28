# ------------------------------------------------------
# Practical No: 6
# Aim: To solve the 8-puzzle (number puzzle) problem using BFS
#      in Python.
# ------------------------------------------------------

# Theory:
# The 8-puzzle consists of a 3x3 board with 8 numbered tiles and one
# blank space (represented by 0). The goal is to reach a target
# arrangement by sliding a tile next to the blank space into the blank
# position. Each arrangement of the board is called a state, and BFS
# is used to search for the shortest sequence of moves to the goal.

# Algorithm:
# 1. Start
# 2. Begin from the given start state
# 3. Find the position of the blank tile (0) and generate all states
#    reachable by sliding an adjacent tile into the blank
# 4. If the goal state is reached, stop and return the path
# 5. Otherwise keep exploring new states using a queue (BFS)
# 6. Stop

# Python Program:

def get_neighbours(state):

    blank_pos = state.index(0)
    row = blank_pos // 3
    col = blank_pos % 3

    moves = []
    if row > 0:
        moves.append(blank_pos - 3)
    if row < 2:
        moves.append(blank_pos + 3)
    if col > 0:
        moves.append(blank_pos - 1)
    if col < 2:
        moves.append(blank_pos + 1)

    neighbours = []
    for new_pos in moves:
        new_state = list(state)
        new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
        neighbours.append(tuple(new_state))

    return neighbours


def solve_puzzle(start, goal):

    queue = [[start]]
    visited = [start]

    while queue:

        path = queue.pop(0)
        state = path[-1]

        if state == goal:
            return path

        for neighbour in get_neighbours(state):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

    return None


start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution_path = solve_puzzle(start_state, goal_state)

print("Goal reached in", len(solution_path) - 1, "moves\n")
for state in solution_path:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print("-----")

# Sample Input / Output:
# Goal reached in 2 moves
# (1, 2, 3)
# (4, 0, 6)
# (7, 5, 8)
# -----
# (1, 2, 3)
# (4, 5, 6)
# (7, 0, 8)
# -----
# (1, 2, 3)
# (4, 5, 6)
# (7, 8, 0)
# -----

# Result:
# The program to solve the 8-puzzle problem using BFS was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What does the blank tile (0) represent in the 8-puzzle?
# 2. Why is BFS guaranteed to find the shortest solution here?
# 3. How many tiles and blank spaces does a standard 8-puzzle have?
# 4. What condition decides which moves are possible for the blank tile?
# 5. Why do we maintain a visited list in this program?
