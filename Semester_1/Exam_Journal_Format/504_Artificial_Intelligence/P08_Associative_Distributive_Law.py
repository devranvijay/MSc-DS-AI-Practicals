# ------------------------------------------------------
# Practical No: 8
# Aim: To verify the Associative Law and Distributive Law of Boolean
#      algebra in Python.
# ------------------------------------------------------

# Theory:
# The Associative Law states that (A AND B) AND C is the same as
# A AND (B AND C), and similarly for OR. The Distributive Law states
# that A AND (B OR C) is the same as (A AND B) OR (A AND C). These
# laws are verified by checking them for every combination of True
# and False values of A, B and C.

# Algorithm:
# 1. Start
# 2. Generate all combinations of True/False for A, B and C
# 3. For each combination, check if the Associative Law holds for AND and OR
# 4. For each combination, check if the Distributive Law holds
# 5. Print the truth table and the final conclusion
# 6. Stop

# Python Program:

values = [True, False]
associative_holds = True
distributive_holds = True

print("A\tB\tC\t(A.B).C\tA.(B.C)\t(A+B)+C\tA+(B+C)")
for a in values:
    for b in values:
        for c in values:
            and_left = (a and b) and c
            and_right = a and (b and c)
            or_left = (a or b) or c
            or_right = a or (b or c)

            print(a, "\t", b, "\t", c, "\t", and_left, "\t", and_right, "\t", or_left, "\t", or_right)

            if and_left != and_right or or_left != or_right:
                associative_holds = False

print("\nAssociative Law holds for all combinations:", associative_holds)

print("\nA\tB\tC\tA.(B+C)\t(A.B)+(A.C)")
for a in values:
    for b in values:
        for c in values:
            left = a and (b or c)
            right = (a and b) or (a and c)
            print(a, "\t", b, "\t", c, "\t", left, "\t", right)
            if left != right:
                distributive_holds = False

print("\nDistributive Law holds for all combinations:", distributive_holds)

# Sample Input / Output:
# (truth table for all 8 combinations of A, B, C is printed)
# Associative Law holds for all combinations: True
# Distributive Law holds for all combinations: True

# Result:
# The program to verify the Associative Law and Distributive Law of
# Boolean algebra was executed successfully and the output was verified.

# Viva Questions:
# 1. State the Associative Law for AND and OR.
# 2. State the Distributive Law for AND over OR.
# 3. Why do we check all combinations of True and False?
# 4. Give the set-theory equivalent of the Distributive Law.
# 5. Why are these laws important in digital logic and AI reasoning?
