# ===== 3b. Using for Loop =====
# Reverse a number using for loop
num = int(input("Enter a number: "))
reverse = 0
n = num
for i in range(len(str(num))):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Original number:", num)
print("Reversed number:", reverse)
