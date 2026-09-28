"""
Practical 03: For and While Loops
Subject : 502 - Essential Technologies for Data Science
Aim     : To demonstrate 'for' loops, 'while' loops, nested loops,
          and loop control statements (break, continue, else) through
          practical examples such as multiplication tables, factorial
          calculation, and prime number detection.
"""


def print_multiplication_table(number: int, upto: int = 10) -> None:
    """Print the multiplication table of `number` from 1 to `upto` using a for loop."""
    print(f"\nMultiplication table of {number} (for loop):")
    for multiplier in range(1, upto + 1):
        print(f"  {number} x {multiplier:2d} = {number * multiplier}")


def calculate_factorial_iterative(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer using a while loop.

    Args:
        number: A non-negative integer.

    Returns:
        The factorial of `number`.

    Raises:
        ValueError: If `number` is negative.
    """
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers.")

    result = 1
    current = number
    while current > 1:
        result *= current
        current -= 1
    return result


def is_prime(number: int) -> bool:
    """Check whether `number` is prime using a for loop with an early exit (break/else)."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    else:
        # The 'else' clause of a for-loop executes only if the loop
        # completed WITHOUT hitting a 'break' statement.
        return True


def find_primes_in_range(start: int, end: int) -> list:
    """Return a list of all prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end + 1) if is_prime(n)]


def demonstrate_nested_loop_pattern(rows: int = 5) -> None:
    """Print a right-angled triangle pattern using nested for loops."""
    print(f"\nNested loop pattern ({rows} rows):")
    for row in range(1, rows + 1):
        print("* " * row)


def demonstrate_break_continue() -> None:
    """Demonstrate 'break' (stop the loop) and 'continue' (skip an iteration)."""
    print("\nDemonstrating 'continue' (skip even numbers 1-10):")
    for number in range(1, 11):
        if number % 2 == 0:
            continue
        print(f"  Odd number: {number}")

    print("\nDemonstrating 'break' (stop once a number > 7 is found):")
    for number in range(1, 11):
        if number > 7:
            print(f"  Breaking loop at {number}")
            break
        print(f"  Checking number: {number}")


def main() -> None:
    """Entry point that drives the loops demonstration."""
    print("=" * 60)
    print("PRACTICAL 03 : FOR AND WHILE LOOPS")
    print("=" * 60)

    print_multiplication_table(number=7)

    factorial_input = 6
    print(f"\nFactorial of {factorial_input} (while loop) = "
          f"{calculate_factorial_iterative(factorial_input)}")

    print(f"\nPrime numbers between 2 and 50:")
    print(find_primes_in_range(2, 50))

    demonstrate_nested_loop_pattern()
    demonstrate_break_continue()

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
