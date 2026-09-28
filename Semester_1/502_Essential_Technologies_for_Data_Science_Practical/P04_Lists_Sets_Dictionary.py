# ------------------------------------------------------
# Practical No: 4
# Aim: To demonstrate list, set and dictionary in Python.
# ------------------------------------------------------

# Theory:
# A list is an ordered collection of items that allows duplicate
# values. A set is an unordered collection of unique items. A
# dictionary stores data in key-value pairs. These are Python's
# built-in data structures used to store and organize data.

# Algorithm:
# 1. Start
# 2. Create a list and perform append, insert and remove operations
# 3. Create two sets and perform union and intersection
# 4. Create a dictionary and perform add, update and display operations
# 5. Stop

# Python Program:

# List operations
fruits = ["apple", "banana", "mango"]
print("Original list:", fruits)

fruits.append("grapes")
print("After append:", fruits)

fruits.insert(1, "orange")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set1:", set1)
print("Set2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Dictionary operations
student = {
    "Name": "Ranvijay",
    "age": 20,
    "Course": "MSC DS AI",
    "Marks": 95,
}
print("Dictionary:", student)

# Accessing a value
print("Student Name:", student["Name"])
print("Marks:", student["Marks"])

# Adding a new key value pair
student["Grade"] = "A"
print("After Adding a Grade:", student)

# update a value
student["Marks"] = 100
print("After updating a marks student:", student)

# removing a key-value pair
del student["age"]
print("After removing age the student is:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# Sample Input / Output:
# Original list: ['apple', 'banana', 'mango']
# After append: ['apple', 'banana', 'mango', 'grapes']
# After insert: ['apple', 'orange', 'banana', 'mango', 'grapes']
# After remove: ['apple', 'orange', 'mango', 'grapes']
# Set1: {1, 2, 3, 4}
# Set2: {3, 4, 5, 6}
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference: {1, 2}
# Dictionary: {'Name': 'Ranvijay', 'age': 20, 'Course': 'MSC DS AI', 'Marks': 95}
# Student Name: Ranvijay
# Marks: 95
# After Adding a Grade: {'Name': 'Ranvijay', 'age': 20, 'Course': 'MSC DS AI', 'Marks': 95, 'Grade': 'A'}
# After updating a marks student: {'Name': 'Ranvijay', 'age': 20, 'Course': 'MSC DS AI', 'Marks': 100, 'Grade': 'A'}
# After removing age the student is: {'Name': 'Ranvijay', 'Course': 'MSC DS AI', 'Marks': 100, 'Grade': 'A'}
# Keys: ['Name', 'Course', 'Marks', 'Grade']
# Values: ['Ranvijay', 'MSC DS AI', 100, 'A']

# Result:
# The program to demonstrate list, set and dictionary operations was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is the difference between a list and a set?
# 2. Can a list contain duplicate values? Can a set?
# 3. How are values accessed in a dictionary?
# 4. What is the difference between append() and insert() in a list?
# 5. Name two set operations and what they do.
# 6. How do you add or update a key-value pair in a dictionary?
# 7. Which statement is used to remove a key-value pair from a dictionary?
