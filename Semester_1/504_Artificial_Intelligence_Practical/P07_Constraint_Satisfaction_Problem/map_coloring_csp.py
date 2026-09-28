"""
Practical 07: Constraint Satisfaction Problem (Map Coloring)
Subject : 504 - Artificial Intelligence
Aim     : To model and solve the Map Coloring problem as a Constraint
          Satisfaction Problem (CSP) using backtracking search, where
          no two adjacent regions may share the same color.
"""


def build_australia_map() -> dict:
    """
    Build the classic 'Map of Australia' CSP adjacency structure.
    Each region maps to the list of regions it shares a border with.
    """
    return {
        "Western Australia": ["Northern Territory", "South Australia"],
        "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
        "South Australia": ["Western Australia", "Northern Territory", "Queensland",
                             "New South Wales", "Victoria"],
        "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
        "New South Wales": ["Queensland", "South Australia", "Victoria"],
        "Victoria": ["South Australia", "New South Wales"],
        "Tasmania": [],  # An island - no shared borders with any other region.
    }


def is_assignment_consistent(region: str, color: str, assignment: dict,
                              adjacency: dict) -> bool:
    """Check that assigning `color` to `region` does not conflict with any assigned neighbor."""
    for neighbor in adjacency[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def select_unassigned_region(adjacency: dict, assignment: dict) -> str:
    """Pick the next unassigned region (simple, in declared order)."""
    for region in adjacency:
        if region not in assignment:
            return region
    return None


def backtracking_search(adjacency: dict, available_colors: list,
                         assignment: dict = None) -> dict:
    """
    Solve the CSP using backtracking search.

    Args:
        adjacency: Region -> list of neighboring regions.
        available_colors: The palette of colors that may be used.
        assignment: The partial assignment built up so far (used internally).

    Returns:
        A complete, consistent assignment {region: color}, or None if
        no solution exists with the given color palette.
    """
    if assignment is None:
        assignment = {}

    if len(assignment) == len(adjacency):
        return assignment

    region = select_unassigned_region(adjacency, assignment)

    for color in available_colors:
        if is_assignment_consistent(region, color, assignment, adjacency):
            assignment[region] = color

            result = backtracking_search(adjacency, available_colors, assignment)
            if result is not None:
                return result

            del assignment[region]  # backtrack

    return None


def main() -> None:
    """Entry point that drives the Map Coloring CSP demonstration."""
    print("=" * 60)
    print("PRACTICAL 07 : CONSTRAINT SATISFACTION PROBLEM (MAP COLORING)")
    print("=" * 60)

    adjacency = build_australia_map()
    available_colors = ["Red", "Green", "Blue"]

    print(f"\nRegions and their neighbors:")
    for region, neighbors in adjacency.items():
        print(f"  {region:<20}: {neighbors}")

    print(f"\nAvailable colors: {available_colors}")

    solution = backtracking_search(adjacency, available_colors)

    if solution:
        print("\nA valid coloring was found:")
        for region, color in solution.items():
            print(f"  {region:<20}: {color}")
    else:
        print("\nNo valid coloring exists with the given palette.")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
