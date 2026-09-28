"""
Practical 09: Predicate Logic
Subject : 504 - Artificial Intelligence
Aim     : To represent facts and rules using First-Order Predicate
          Logic, and implement a simple forward-chaining inference
          engine that derives new facts from existing ones - the same
          principle used by Prolog and rule-based expert systems.

Example knowledge base (in predicate-logic notation):
    Fact : man(socrates)
    Fact : man(plato)
    Rule : man(X) -> mortal(X)          "For all X, if X is a man, X is mortal."
    Rule : mortal(X) ^ man(X) -> human(X)
"""


class KnowledgeBase:
    """
    A minimal predicate-logic knowledge base supporting single-argument
    predicates, unit facts, and Horn-clause-style implication rules,
    with a forward-chaining inference procedure.
    """

    def __init__(self) -> None:
        self.facts = set()          # e.g. {("man", "socrates"), ...}
        self.rules = []             # e.g. [(["man"], "mortal"), ...]

    def add_fact(self, predicate: str, entity: str) -> None:
        """Add a ground fact, e.g. add_fact('man', 'socrates') means man(socrates)."""
        self.facts.add((predicate, entity))

    def add_rule(self, premises: list, conclusion: str) -> None:
        """
        Add an inference rule of the form:
            premise_1(X) ^ premise_2(X) ^ ... -> conclusion(X)
        meaning: if an entity X satisfies ALL premise predicates,
        then conclusion(X) can be inferred.
        """
        self.rules.append((premises, conclusion))

    def get_all_entities(self) -> set:
        """Return every distinct entity mentioned anywhere in the knowledge base."""
        return {entity for _, entity in self.facts}

    def forward_chain(self) -> list:
        """
        Repeatedly apply rules to derive new facts until no more new
        facts can be added (fixed-point / forward-chaining inference).

        Returns:
            A list of (predicate, entity, rule_used) for every fact
            newly derived (not originally asserted).
        """
        derived_facts = []
        entities = self.get_all_entities()
        changed = True

        while changed:
            changed = False

            for entity in entities:
                for premises, conclusion in self.rules:
                    already_known = (conclusion, entity) in self.facts
                    premises_satisfied = all(
                        (premise, entity) in self.facts for premise in premises
                    )

                    if premises_satisfied and not already_known:
                        self.facts.add((conclusion, entity))
                        rule_description = f"{' AND '.join(premises)} -> {conclusion}"
                        derived_facts.append((conclusion, entity, rule_description))
                        changed = True

        return derived_facts

    def query(self, predicate: str, entity: str) -> bool:
        """Check whether predicate(entity) is known to be true in the knowledge base."""
        return (predicate, entity) in self.facts


def build_socrates_knowledge_base() -> KnowledgeBase:
    """Build the classic 'All men are mortal' predicate-logic knowledge base."""
    knowledge_base = KnowledgeBase()

    knowledge_base.add_fact("man", "socrates")
    knowledge_base.add_fact("man", "plato")
    knowledge_base.add_fact("woman", "athena")

    # Rule: For all X, man(X) implies mortal(X).
    knowledge_base.add_rule(premises=["man"], conclusion="mortal")
    # Rule: For all X, woman(X) implies mortal(X).
    knowledge_base.add_rule(premises=["woman"], conclusion="mortal")
    # Rule: For all X, mortal(X) AND man(X) implies human(X).
    knowledge_base.add_rule(premises=["mortal", "man"], conclusion="human")

    return knowledge_base


def main() -> None:
    """Entry point that drives the predicate-logic inference demonstration."""
    print("=" * 60)
    print("PRACTICAL 09 : PREDICATE LOGIC (FORWARD-CHAINING INFERENCE)")
    print("=" * 60)

    knowledge_base = build_socrates_knowledge_base()

    print("\nInitial facts:")
    for predicate, entity in sorted(knowledge_base.facts):
        print(f"  {predicate}({entity})")

    print("\nRules:")
    for premises, conclusion in knowledge_base.rules:
        print(f"  {' AND '.join(f'{p}(X)' for p in premises)} -> {conclusion}(X)")

    derived = knowledge_base.forward_chain()

    print("\nNewly derived facts (via forward chaining):")
    for predicate, entity, rule_used in derived:
        print(f"  {predicate}({entity})   [via rule: {rule_used}]")

    print("\nSample queries:")
    for predicate, entity in [("mortal", "socrates"), ("human", "socrates"),
                               ("mortal", "athena"), ("human", "athena")]:
        result = knowledge_base.query(predicate, entity)
        print(f"  Is {predicate}({entity}) true?  -> {result}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
