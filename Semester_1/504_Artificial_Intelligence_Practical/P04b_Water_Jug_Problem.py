# ------------------------------------------------------
# Practical No: 4 (b)
# Aim: To solve the Water Jug problem using BFS in Python.
# ------------------------------------------------------

# Theory:
# The Water Jug problem asks us to measure an exact quantity of water
# using two jugs of given capacities, with no other measuring
# equipment. The allowed operations are: fill a jug completely, empty
# a jug completely, or pour water from one jug into the other. It can
# be solved by treating every (jugA, jugB) combination as a state and
# searching through the states using BFS.

# Algorithm:
# 1. Start
# 2. Begin from the state (0, 0)
# 3. From the current state, generate all possible next states
#    (fill, empty, pour)
# 4. If the target amount is reached in either jug, stop and return the path
# 5. Otherwise continue exploring new states using a queue (BFS)
# 6. Stop

# Python Program:

def get_next_states(state, cap_a, cap_b):

    a, b = state

    return [
        (cap_a, b),
        (a, cap_b),
        (0, b),
        (a, 0),
        (a - min(a, cap_b - b), b + min(a, cap_b - b)),
        (a + min(b, cap_a - a), b - min(b, cap_a - a)),
    ]


def solve_water_jug(cap_a, cap_b, target):

    queue = [[(0, 0)]]
    visited = [(0, 0)]

    while queue:

        path = queue.pop(0)
        a, b = path[-1]

        if a == target or b == target:
            return path

        for state in get_next_states((a, b), cap_a, cap_b):
            if state not in visited:
                visited.append(state)
                queue.append(path + [state])

    return None


solution = solve_water_jug(cap_a=4, cap_b=3, target=2)

print("Solution path (Jug A, Jug B):")
for state in solution:
    print(state)

# Sample Input / Output:
# Solution path (Jug A, Jug B):
# (0, 0)
# (0, 3)
# (3, 0)
# (3, 3)
# (4, 2)

# Result:
# The program to solve the Water Jug problem using BFS was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What are the three allowed operations in the Water Jug problem?
# 2. Why is BFS suitable for solving this problem optimally?
# 3. What does a "state" represent in this problem?
# 4. Why do we maintain a visited list?
# 5. Can the Water Jug problem be solved using DFS? What is the drawback?
