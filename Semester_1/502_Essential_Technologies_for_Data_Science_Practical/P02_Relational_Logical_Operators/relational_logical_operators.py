"""
Practical 02: Relational and Logical Operators
Subject : 502 - Essential Technologies for Data Science
Aim     : To demonstrate relational operators (==, !=, >, <, >=, <=)
          and logical operators (and, or, not) with real examples,
          including short-circuit evaluation.
"""


def demonstrate_relational_operators(a: float, b: float) -> None:
    """Print the result of every relational operator applied to a and b."""
    print(f"\nComparing a = {a} and b = {b}")
    print("-" * 50)
    print(f"a == b : {a == b}")
    print(f"a != b : {a != b}")
    print(f"a >  b : {a > b}")
    print(f"a <  b : {a < b}")
    print(f"a >= b : {a >= b}")
    print(f"a <= b : {a <= b}")


def demonstrate_logical_operators(age: int, has_id_card: bool) -> None:
    """
    Demonstrate 'and', 'or', 'not' using a real-world eligibility example:
    a person can vote only if they are 18+ AND hold a valid ID card.
    """
    print(f"\nAge = {age}, Has ID card = {has_id_card}")
    print("-" * 50)

    is_adult = age >= 18
    can_vote = is_adult and has_id_card
    can_apply_for_id = is_adult or has_id_card
    id_missing = not has_id_card

    print(f"is_adult (age >= 18)               : {is_adult}")
    print(f"can_vote (is_adult AND has_id_card) : {can_vote}")
    print(f"can_apply_for_id (is_adult OR id)   : {can_apply_for_id}")
    print(f"id_missing (NOT has_id_card)        : {id_missing}")


def demonstrate_short_circuit_evaluation() -> None:
    """
    Show that Python's 'and'/'or' operators short-circuit, i.e. they stop
    evaluating as soon as the final result is already determined.
    """

    def noisy_true() -> bool:
        print("  -> noisy_true() was called")
        return True

    def noisy_false() -> bool:
        print("  -> noisy_false() was called")
        return False

    print("\nEvaluating: noisy_false() and noisy_true()")
    result_and = noisy_false() and noisy_true()
    print(f"Result: {result_and}  (noisy_true was never called - short circuit)")

    print("\nEvaluating: noisy_true() or noisy_false()")
    result_or = noisy_true() or noisy_false()
    print(f"Result: {result_or}  (noisy_false was never called - short circuit)")


def main() -> None:
    """Entry point that drives the relational/logical operator demonstration."""
    print("=" * 60)
    print("PRACTICAL 02 : RELATIONAL AND LOGICAL OPERATORS")
    print("=" * 60)

    demonstrate_relational_operators(a=25, b=40)
    demonstrate_logical_operators(age=20, has_id_card=True)
    demonstrate_logical_operators(age=16, has_id_card=False)
    demonstrate_short_circuit_evaluation()

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
