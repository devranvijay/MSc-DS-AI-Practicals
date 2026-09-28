"""
Practical 02b: Tower of Hanoi
Subject : 504 - Artificial Intelligence
Aim     : To solve the Tower of Hanoi puzzle using recursion, and to
          count the minimum number of moves required.
"""


def solve_tower_of_hanoi(num_disks: int, source: str, auxiliary: str,
                          destination: str, move_log: list) -> None:
    """
    Recursively solve the Tower of Hanoi puzzle.

    Args:
        num_disks: Number of disks to move.
        source: Name of the source peg.
        auxiliary: Name of the helper peg.
        destination: Name of the destination peg.
        move_log: A list that accumulates a human-readable log of each move.
    """
    if num_disks == 0:
        return

    # Step 1: Move the top (num_disks - 1) disks out of the way, to the auxiliary peg.
    solve_tower_of_hanoi(num_disks - 1, source, destination, auxiliary, move_log)

    # Step 2: Move the largest remaining disk directly to the destination peg.
    move_log.append(f"Move disk {num_disks} from {source} -> {destination}")

    # Step 3: Move the (num_disks - 1) disks from the auxiliary peg onto the destination.
    solve_tower_of_hanoi(num_disks - 1, auxiliary, source, destination, move_log)


def minimum_moves_required(num_disks: int) -> int:
    """Return the minimum number of moves required to solve Tower of Hanoi (2^n - 1)."""
    return (2 ** num_disks) - 1


def main() -> None:
    """Entry point that drives the Tower of Hanoi demonstration."""
    print("=" * 60)
    print("PRACTICAL 02b : TOWER OF HANOI (RECURSION)")
    print("=" * 60)

    num_disks = 4
    move_log = []
    solve_tower_of_hanoi(num_disks, source="A", auxiliary="B", destination="C",
                          move_log=move_log)

    print(f"\nNumber of disks: {num_disks}")
    print(f"Pegs           : A (source), B (auxiliary), C (destination)\n")
    for step_number, move in enumerate(move_log, start=1):
        print(f"  Step {step_number:2d}: {move}")

    print(f"\nTotal moves made    : {len(move_log)}")
    print(f"Minimum moves needed: {minimum_moves_required(num_disks)} (2^n - 1)")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
