# Accept two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Arithmetic operations
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
# Division
if num2 != 0:
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)
    print("Modulus =", num1 % num2)
else:
    print("Division, Floor Division and Modulus are not possible by zero.")
# Exponentiation
print("Power =", num1 ** num2)
