# . List
print("----- LIST -----")
students = ["Amit", "Riya", "John", "Sneha"]
print("Original List:", students)
# Adding an element
students.append("Rahul")
print("After adding:", students)
# Accessing an element
print("First student:", students[0])
# Removing an element
students.remove("John")
print("After removing:", students)
# 2. Set
print("\n----- SET -----")
numbers = {10, 20, 30, 20, 40, 10}
print("Set:", numbers)   # Duplicate values are automatically removed
# Adding an element
numbers.add(50)
print("After adding:", numbers)
# Removing an element
numbers.remove(20)
print("After removing:", numbers)
# 3. Dictionary
print("\n----- DICTIONARY -----")
student = {
    "Name": "Amit",
    "Age": 20,
    "Course": "MScIT",
    "Marks": 85
}
print("Dictionary:", student)
# Accessing a value
print("Student Name:", student["Name"])
# Adding a new key-value pair
student["Grade"] = "A"
print("After adding Grade:", student)
# Updating a value
student["Marks"] = 90
print("After updating Marks:", student)
# Removing a key-value pair
del student["Age"]
print("After removing Age:", student)
