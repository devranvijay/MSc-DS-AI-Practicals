# ===== 3a. Using while Loop =====
# Reverse a number using while loop
num = int(input("Enter a number: "))
reverse = 0
n = num
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Original number:", num)
print("Reversed number:", reverse)
