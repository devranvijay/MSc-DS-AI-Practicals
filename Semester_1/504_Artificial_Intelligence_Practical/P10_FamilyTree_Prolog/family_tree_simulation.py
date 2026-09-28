"""
Practical 10: Family Tree using Prolog-style Predicates (Python Simulation)
Subject : 504 - Artificial Intelligence
Aim     : To represent a family tree using logical facts (parent,
          male, female) and derive relationships (father, mother,
          sibling, grandparent, uncle, aunt, ancestor) via rule-based
          inference - mirroring the accompanying `family_tree.pl`
          Prolog source, so the practical can also be verified without
          requiring a separate SWI-Prolog installation.

See also: family_tree.pl (the equivalent, original Prolog program).
"""


def build_family_facts() -> tuple:
    """
    Define the same facts as family_tree.pl:
    parent relationships, and each person's gender.
    """
    parent_of = [
        ("dinesh", "ramesh"), ("dinesh", "suresh"),
        ("sunita", "ramesh"), ("sunita", "suresh"),
        ("ramesh", "aditi"), ("ramesh", "arjun"),
        ("kavita", "aditi"), ("kavita", "arjun"),
        ("suresh", "meera"), ("vandana", "meera"),
    ]

    male_people = {"dinesh", "ramesh", "suresh", "arjun"}
    female_people = {"sunita", "kavita", "vandana", "aditi", "meera"}

    return parent_of, male_people, female_people


class FamilyTree:
    """A small inference engine that mirrors the Prolog rules in family_tree.pl."""

    def __init__(self, parent_of: list, male_people: set, female_people: set) -> None:
        self.parent_of = parent_of
        self.male_people = male_people
        self.female_people = female_people

    def is_parent(self, parent: str, child: str) -> bool:
        """Equivalent to Prolog: parent(Parent, Child)."""
        return (parent, child) in self.parent_of

    def get_parents(self, person: str) -> list:
        """Return all parents of a given person."""
        return [parent for parent, child in self.parent_of if child == person]

    def get_children(self, person: str) -> list:
        """Return all children of a given person."""
        return [child for parent, child in self.parent_of if parent == person]

    def father(self, person: str) -> list:
        """Equivalent to Prolog: father(Father, Child)."""
        return [p for p in self.get_parents(person) if p in self.male_people]

    def mother(self, person: str) -> list:
        """Equivalent to Prolog: mother(Mother, Child)."""
        return [p for p in self.get_parents(person) if p in self.female_people]

    def siblings(self, person: str) -> set:
        """Equivalent to Prolog: sibling(PersonA, PersonB)."""
        shared_parents = self.get_parents(person)
        sibling_set = set()
        for parent in shared_parents:
            for child in self.get_children(parent):
                if child != person:
                    sibling_set.add(child)
        return sibling_set

    def grandparents(self, person: str) -> set:
        """Equivalent to Prolog: grandparent(Grandparent, Grandchild)."""
        grandparent_set = set()
        for parent in self.get_parents(person):
            grandparent_set.update(self.get_parents(parent))
        return grandparent_set

    def uncles_and_aunts(self, person: str) -> set:
        """Equivalent to Prolog: uncle/aunt(UncleOrAunt, Person)."""
        result = set()
        for parent in self.get_parents(person):
            result.update(self.siblings(parent))
        return result

    def ancestors(self, person: str) -> set:
        """Equivalent to Prolog: recursive ancestor(Ancestor, Descendant)."""
        direct_parents = self.get_parents(person)
        all_ancestors = set(direct_parents)
        for parent in direct_parents:
            all_ancestors.update(self.ancestors(parent))
        return all_ancestors


def main() -> None:
    """Entry point that drives the family-tree relationship demonstration."""
    print("=" * 60)
    print("PRACTICAL 10 : FAMILY TREE USING PROLOG-STYLE PREDICATES")
    print("=" * 60)
    print("\n(This is a Python simulation of the logic in family_tree.pl,")
    print(" so the practical runs without requiring SWI-Prolog to be installed.)")

    parent_of, male_people, female_people = build_family_facts()
    family = FamilyTree(parent_of, male_people, female_people)

    print("\nFacts (parent relationships):")
    for parent, child in parent_of:
        print(f"  parent({parent}, {child})")

    print("\n--- Derived relationships for 'aditi' ---")
    print(f"father(aditi)            : {family.father('aditi')}")
    print(f"mother(aditi)            : {family.mother('aditi')}")
    print(f"siblings(aditi)          : {family.siblings('aditi')}")
    print(f"grandparents(aditi)      : {family.grandparents('aditi')}")
    print(f"uncles/aunts(aditi)      : {family.uncles_and_aunts('aditi')}")
    print(f"ancestors(aditi)         : {family.ancestors('aditi')}")

    print("\n--- Derived relationships for 'meera' ---")
    print(f"father(meera)            : {family.father('meera')}")
    print(f"grandparents(meera)      : {family.grandparents('meera')}")
    print(f"ancestors(meera)         : {family.ancestors('meera')}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
