"""
Practical 04: Lists, Sets, and Dictionaries
Subject : 502 - Essential Technologies for Data Science
Aim     : To demonstrate creation, manipulation, and common operations
          on Python's core built-in data structures: list, set, and
          dictionary, including comprehensions.
"""


def demonstrate_list_operations() -> None:
    """Demonstrate common list operations: append, insert, remove, slicing, sorting."""
    print("\n--- LIST OPERATIONS ---")
    students = ["Aditi", "Rohan", "Meera"]
    print(f"Initial list       : {students}")

    students.append("Karan")
    print(f"After append       : {students}")

    students.insert(1, "Sanjay")
    print(f"After insert at 1  : {students}")

    students.remove("Meera")
    print(f"After remove       : {students}")

    print(f"Sliced [1:3]       : {students[1:3]}")
    print(f"Sorted copy        : {sorted(students)}")
    print(f"Reversed copy      : {list(reversed(students))}")

    squares = [number ** 2 for number in range(1, 6)]
    print(f"List comprehension (squares 1-5): {squares}")


def demonstrate_set_operations() -> None:
    """Demonstrate set operations: union, intersection, difference, symmetric difference."""
    print("\n--- SET OPERATIONS ---")
    python_students = {"Aditi", "Rohan", "Meera", "Karan"}
    ai_students = {"Rohan", "Karan", "Divya", "Priya"}

    print(f"Python course students : {python_students}")
    print(f"AI course students     : {ai_students}")
    print(f"Union (either course)  : {python_students | ai_students}")
    print(f"Intersection (both)    : {python_students & ai_students}")
    print(f"Difference (only Python): {python_students - ai_students}")
    print(f"Symmetric diff (exactly one course): "
          f"{python_students ^ ai_students}")


def demonstrate_dictionary_operations() -> None:
    """Demonstrate dictionary creation, access, update, and comprehension."""
    print("\n--- DICTIONARY OPERATIONS ---")
    student_marks = {"Aditi": 88, "Rohan": 72, "Meera": 95, "Karan": 60}
    print(f"Initial dictionary : {student_marks}")

    student_marks["Divya"] = 78
    print(f"After adding Divya : {student_marks}")

    student_marks["Rohan"] = 75
    print(f"After updating Rohan's marks: {student_marks}")

    print(f"Keys   : {list(student_marks.keys())}")
    print(f"Values : {list(student_marks.values())}")
    print(f"Items  : {list(student_marks.items())}")

    grade_book = {
        name: ("Distinction" if marks >= 85 else "First Class" if marks >= 60 else "Pass")
        for name, marks in student_marks.items()
    }
    print(f"Dictionary comprehension (grades): {grade_book}")

    topper = max(student_marks, key=student_marks.get)
    print(f"Topper: {topper} with {student_marks[topper]} marks")


def main() -> None:
    """Entry point that drives the data-structure demonstration."""
    print("=" * 60)
    print("PRACTICAL 04 : LISTS, SETS, AND DICTIONARIES")
    print("=" * 60)

    demonstrate_list_operations()
    demonstrate_set_operations()
    demonstrate_dictionary_operations()

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
