"""
Practical 01: Arithmetic Operations in Python
Subject : 502 - Essential Technologies for Data Science
Aim     : To implement and demonstrate all basic arithmetic operators
          available in Python (+, -, *, /, //, %, **) along with
          operator precedence and augmented assignment operators.

Author  : Data Science & AI Practical Repository
"""


def basic_arithmetic(a: float, b: float) -> dict:
    """
    Perform the standard arithmetic operations on two numbers.

    Args:
        a: The first operand.
        b: The second operand (must be non-zero for division/modulus).

    Returns:
        A dictionary mapping the operation name to its result.

    Raises:
        ZeroDivisionError: If `b` is zero and a division-based
            operation is requested.
    """
    results = {
        "Addition (a + b)": a + b,
        "Subtraction (a - b)": a - b,
        "Multiplication (a * b)": a * b,
        "Exponentiation (a ** b)": a ** b,
    }

    if b == 0:
        results["Division (a / b)"] = "Undefined (division by zero)"
        results["Floor Division (a // b)"] = "Undefined (division by zero)"
        results["Modulus (a % b)"] = "Undefined (division by zero)"
    else:
        results["Division (a / b)"] = a / b
        results["Floor Division (a // b)"] = a // b
        results["Modulus (a % b)"] = a % b

    return results


def demonstrate_operator_precedence() -> None:
    """Show how Python evaluates a mixed arithmetic expression using BODMAS rules."""
    expression = "10 + 2 * 3 ** 2 - (4 / 2)"
    value = 10 + 2 * 3 ** 2 - (4 / 2)
    print(f"\nExpression : {expression}")
    print(f"Evaluated  : {value}")
    print("Explanation: ** first, then *, then + and - left to right, "
          "brackets evaluated first.")


def demonstrate_augmented_assignment() -> None:
    """Demonstrate shorthand augmented assignment operators (+=, -=, *=, etc.)."""
    counter = 10
    print(f"\nInitial value of counter : {counter}")

    counter += 5
    print(f"After counter += 5       : {counter}")

    counter -= 3
    print(f"After counter -= 3       : {counter}")

    counter *= 2
    print(f"After counter *= 2       : {counter}")

    counter //= 4
    print(f"After counter //= 4      : {counter}")

    counter **= 3
    print(f"After counter **= 3      : {counter}")


def get_numeric_input(prompt: str, default: float) -> float:
    """
    Safely read a numeric value from the user, falling back to a default
    when running in a non-interactive environment or on invalid input.
    """
    try:
        raw_value = input(prompt)
        return float(raw_value)
    except (ValueError, EOFError):
        print(f"(Using default value: {default})")
        return default


def main() -> None:
    """Entry point that drives the arithmetic operations demonstration."""
    print("=" * 60)
    print("PRACTICAL 01 : ARITHMETIC OPERATIONS IN PYTHON")
    print("=" * 60)

    first_number = get_numeric_input("Enter the first number  : ", 15)
    second_number = get_numeric_input("Enter the second number : ", 4)

    print(f"\nOperands -> a = {first_number}, b = {second_number}")
    print("-" * 60)

    outcomes = basic_arithmetic(first_number, second_number)
    for operation_name, outcome in outcomes.items():
        print(f"{operation_name:<28}: {outcome}")

    demonstrate_operator_precedence()
    demonstrate_augmented_assignment()

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
