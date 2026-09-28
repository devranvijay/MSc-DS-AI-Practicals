# ------------------------------------------------------
# Practical No: 3
# Aim: To demonstrate for loop and while loop in Python.
# ------------------------------------------------------

# Theory:
# A for loop is used to iterate over a sequence of known length,
# such as range(). A while loop repeats a block of statements as
# long as a given condition remains true. Loops are used to avoid
# writing repetitive code.

# Algorithm:
# 1. Start
# 2. Read a number
# 3. Using for loop, print its multiplication table
# 4. Using while loop, find the factorial of the number
# 5. Display the results
# 6. Stop

# Python Program:

num = int(input("Enter a number: "))

print("Multiplication table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

fact = 1
n = num
while n > 1:
    fact = fact * n
    n = n - 1

print("Factorial of", num, "is", fact)

# Sample Input / Output:
# Enter a number: 5
# Multiplication table of 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50
# Factorial of 5 is 120

# Result:
# The program to demonstrate for loop and while loop was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What is the difference between a for loop and a while loop?
# 2. What does the range() function do?
# 3. What is an infinite loop? How can it occur in a while loop?
# 4. What is the use of the break and continue statements?
# 5. How is factorial of a number calculated using a loop?
