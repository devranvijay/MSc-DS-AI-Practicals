# ------------------------------------------------------
# Practical No: 3 (b)
# Aim: To implement the Hill Climbing algorithm in Python.
# ------------------------------------------------------

# Theory:
# Hill Climbing is a local search algorithm that starts with a random
# solution and keeps moving to a better neighboring solution. It stops
# when no neighbor gives a better result, which may be a local maximum
# rather than the global maximum.

# Algorithm:
# 1. Start
# 2. Choose a starting point
# 3. Look at the neighboring points (one step left and one step right)
# 4. If a neighbor has a higher value, move to that neighbor
# 5. If no neighbor is better, stop (a peak has been reached)
# 6. Stop

# Python Program:

def f(x):
    return -(x - 5) ** 2 + 25       # a simple function with maximum at x = 5


def hill_climbing(start_x, step):

    current_x = start_x

    while True:

        current_value = f(current_x)
        left_value = f(current_x - step)
        right_value = f(current_x + step)

        if right_value > current_value:
            current_x = current_x + step
        elif left_value > current_value:
            current_x = current_x - step
        else:
            break

    return current_x


best_x = hill_climbing(start_x=0, step=1)
print("Best x found =", best_x)
print("Maximum value of function =", f(best_x))

# Sample Input / Output:
# Best x found = 5
# Maximum value of function = 25

# Result:
# The program to implement the Hill Climbing algorithm was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What is a local maximum in Hill Climbing?
# 2. Why can Hill Climbing fail to find the global maximum?
# 3. What is a neighboring state in Hill Climbing?
# 4. Name one method to overcome the local maximum problem.
# 5. Is Hill Climbing a complete algorithm? Why or why not?
