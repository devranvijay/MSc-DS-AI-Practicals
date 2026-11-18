# Predicate Logic Program
facts = {
    ("batsman", "Sachin")
}
rules = {
    ("batsman", "cricketer")
}
# Derive new predicate
for fact in list(facts):
    for rule in rules:
        if fact[0] == rule[0]:
            new_fact = (rule[1], fact[1])
            facts.add(new_fact)
print("Given Fact: Sachin is a batsman")
print("Rule: Batsman is a cricketer")
print("\nDerived Predicate:")
for predicate, person in facts:
    if predicate == "cricketer":
        print(person, "is a", predicate)
