# ------------------------------------------------------
# Practical No: 2
# Aim: To perform relational and logical operations in Python.
# ------------------------------------------------------

# Theory:
# Relational operators compare two values and return True or False.
# The relational operators are ==, !=, >, <, >=, <=.
# Logical operators (and, or, not) combine two or more conditions
# and are commonly used in decision making.

# Algorithm:
# 1. Start
# 2. Read two numbers a and b
# 3. Apply relational operators on a and b
# 4. Read age and check logical condition for voting eligibility
# 5. Display the results
# 6. Stop

# Python Program:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID card (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You are eligible to vote")
else:
    print("You are NOT eligible to vote")

print("NOT condition example, not (age >= 18) =", not (age >= 18))

# Sample Input / Output:
# Enter first number: 25
# Enter second number: 40
# a == b : False
# a != b : True
# a > b  : False
# a < b  : True
# a >= b : False
# a <= b : True
# Enter your age: 20
# Do you have a valid ID card (yes/no): yes
# You are eligible to vote
# NOT condition example, not (age >= 18) = False

# Result:
# The program to demonstrate relational and logical operators was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is the difference between = and == in Python?
# 2. List all the relational operators available in Python.
# 3. What do the logical operators and, or, not do?
# 4. What is short circuit evaluation?
# 5. What will "5 > 3 and 2 > 4" evaluate to?
