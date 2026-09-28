"""
Practical 08: Associative and Distributive Laws (Boolean Algebra & Set Theory)
Subject : 504 - Artificial Intelligence
Aim     : To verify the Associative Law and Distributive Law using
          both Boolean algebra (AND/OR) and Set theory (union/
          intersection), by exhaustively testing all truth-value /
          set combinations - a form of automated logical proof used
          in AI knowledge representation.
"""

from itertools import product


def verify_boolean_associative_law() -> bool:
    """
    Verify the Associative Law for Boolean AND and OR:
        (A AND B) AND C == A AND (B AND C)
        (A OR B)  OR C  == A OR (B OR C)
    over every combination of True/False for A, B, C.
    """
    print("\n--- BOOLEAN ASSOCIATIVE LAW ---")
    all_hold = True

    for a, b, c in product([True, False], repeat=3):
        and_left = (a and b) and c
        and_right = a and (b and c)

        or_left = (a or b) or c
        or_right = a or (b or c)

        holds = (and_left == and_right) and (or_left == or_right)
        all_hold = all_hold and holds

        print(f"A={a!s:<5} B={b!s:<5} C={c!s:<5} | "
              f"(A.B).C={and_left!s:<5} A.(B.C)={and_right!s:<5} | "
              f"(A+B)+C={or_left!s:<5} A+(B+C)={or_right!s:<5} | Holds={holds}")

    return all_hold


def verify_boolean_distributive_law() -> bool:
    """
    Verify the Distributive Law for Boolean algebra:
        A AND (B OR C)  == (A AND B) OR (A AND C)
        A OR  (B AND C) == (A OR B) AND (A OR C)
    over every combination of True/False for A, B, C.
    """
    print("\n--- BOOLEAN DISTRIBUTIVE LAW ---")
    all_hold = True

    for a, b, c in product([True, False], repeat=3):
        left_1 = a and (b or c)
        right_1 = (a and b) or (a and c)

        left_2 = a or (b and c)
        right_2 = (a or b) and (a or c)

        holds = (left_1 == right_1) and (left_2 == right_2)
        all_hold = all_hold and holds

        print(f"A={a!s:<5} B={b!s:<5} C={c!s:<5} | "
              f"A.(B+C)={left_1!s:<5} (A.B)+(A.C)={right_1!s:<5} | Holds={holds}")

    return all_hold


def verify_set_associative_law() -> bool:
    """Verify the Associative Law for set Union and Intersection."""
    print("\n--- SET THEORY ASSOCIATIVE LAW ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    set_c = {3, 4, 5}

    union_left = (set_a | set_b) | set_c
    union_right = set_a | (set_b | set_c)

    intersection_left = (set_a & set_b) & set_c
    intersection_right = set_a & (set_b & set_c)

    print(f"A={set_a}, B={set_b}, C={set_c}")
    print(f"(A U B) U C = {union_left}  |  A U (B U C) = {union_right}  "
          f"| Equal = {union_left == union_right}")
    print(f"(A n B) n C = {intersection_left}  |  A n (B n C) = {intersection_right}  "
          f"| Equal = {intersection_left == intersection_right}")

    return union_left == union_right and intersection_left == intersection_right


def verify_set_distributive_law() -> bool:
    """Verify the Distributive Law for set Union and Intersection."""
    print("\n--- SET THEORY DISTRIBUTIVE LAW ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    set_c = {3, 4, 5}

    left_1 = set_a & (set_b | set_c)
    right_1 = (set_a & set_b) | (set_a & set_c)

    left_2 = set_a | (set_b & set_c)
    right_2 = (set_a | set_b) & (set_a | set_c)

    print(f"A n (B U C) = {left_1}  |  (A n B) U (A n C) = {right_1}  "
          f"| Equal = {left_1 == right_1}")
    print(f"A U (B n C) = {left_2}  |  (A U B) n (A U C) = {right_2}  "
          f"| Equal = {left_2 == right_2}")

    return left_1 == right_1 and left_2 == right_2


def main() -> None:
    """Entry point that drives the Associative/Distributive law verification."""
    print("=" * 60)
    print("PRACTICAL 08 : ASSOCIATIVE AND DISTRIBUTIVE LAWS")
    print("=" * 60)

    boolean_associative_holds = verify_boolean_associative_law()
    boolean_distributive_holds = verify_boolean_distributive_law()
    set_associative_holds = verify_set_associative_law()
    set_distributive_holds = verify_set_distributive_law()

    print("\n--- SUMMARY ---")
    print(f"Boolean Associative Law holds for ALL combinations : {boolean_associative_holds}")
    print(f"Boolean Distributive Law holds for ALL combinations: {boolean_distributive_holds}")
    print(f"Set Associative Law holds                          : {set_associative_holds}")
    print(f"Set Distributive Law holds                         : {set_distributive_holds}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
