# ------------------------------------------------------
# Practical No: 2 (b)
# Aim: To solve the Tower of Hanoi problem using recursion in Python.
# ------------------------------------------------------

# Theory:
# Tower of Hanoi is a puzzle where disks must be moved from a source
# peg to a destination peg, using an auxiliary peg, following the
# rule that a larger disk can never be placed on a smaller disk.
# It is a classic example solved using recursion.

# Algorithm:
# 1. Start
# 2. If there is only one disk, move it directly from source to destination
# 3. Otherwise, move the top (n-1) disks from source to auxiliary
# 4. Move the largest disk from source to destination
# 5. Move the (n-1) disks from auxiliary to destination
# 6. Stop

# Python Program:

def hanoi(n, source, aux, dest):
    if n == 1:
        print("Move disk 1 from", source, "to", dest)
        return
    hanoi(n - 1, source, dest, aux)
    print("Move disk", n, "from", source, "to", dest)
    hanoi(n - 1, aux, source, dest)


num_disks = 3
hanoi(num_disks, "A", "B", "C")

total_moves = 2 ** num_disks - 1
print("Total moves required =", total_moves)

# Sample Input / Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Total moves required = 7

# Result:
# The program to solve the Tower of Hanoi problem using recursion was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is the minimum number of moves required for n disks?
# 2. What is the base case in the Tower of Hanoi recursion?
# 3. Why can a larger disk never be placed on a smaller disk?
# 4. What is the role of the auxiliary peg?
# 5. What is the time complexity of the Tower of Hanoi solution?
