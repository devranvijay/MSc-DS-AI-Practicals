# Family Relations using Predicates
# Facts
male = ['John', 'David', 'Rahul', 'Amit']
female = ['Mary', 'Lisa', 'Priya', 'Neha']
parent = [
    ('John', 'David'),
    ('Mary', 'David'),
    ('John', 'Lisa'),
    ('Mary', 'Lisa'),
    ('David', 'Rahul'),
    ('Priya', 'Rahul'),
    ('David', 'Neha'),
    ('Priya', 'Neha'),
    ('Lisa', 'Amit')
]
# Basic predicates
def is_parent(x, y):
    return (x, y) in parent
def is_male(x):
    return x in male
def is_female(x):
    return x in female
# Family relation rules
def father(x, y):
    return is_male(x) and is_parent(x, y)
def mother(x, y):
    return is_female(x) and is_parent(x, y)
def grandfather(x, y):
    return is_male(x) and any(
        is_parent(x, z) and is_parent(z, y)
        for z in male + female
    )
def grandmother(x, y):
    return is_female(x) and any(
        is_parent(x, z) and is_parent(z, y)
        for z in male + female
    )
def sibling(x, y):
    return x != y and any(
        is_parent(p, x) and is_parent(p, y)
        for p in male + female
    )
def brother(x, y):
    return is_male(x) and sibling(x, y)
def sister(x, y):
    return is_female(x) and sibling(x, y)
def uncle(x, y):
    return is_male(x) and any(
        sibling(x, z) and is_parent(z, y)
        for z in male + female
    )
def aunt(x, y):
    return is_female(x) and any(
        sibling(x, z) and is_parent(z, y)
        for z in male + female
    )
def nephew(x, y):
    return is_male(x) and any(
        sibling(y, z) and is_parent(z, x)
        for z in male + female
    )
def niece(x, y):
    return is_female(x) and any(
        sibling(y, z) and is_parent(z, x)
        for z in male + female
    )
def cousin(x, y):
    return x != y and any(
        sibling(p, q) and is_parent(p, x)
        and is_parent(q, y)
        for p in male + female
        for q in male + female
    )
# Display family relations
print("FAMILY RELATIONS")
for x in male + female:
    for y in male + female:
        if father(x, y):
            print(x, "is father of", y)
        if mother(x, y):
            print(x, "is mother of", y)
        if grandfather(x, y):
            print(x, "is grandfather of", y)
        if grandmother(x, y):
            print(x, "is grandmother of", y)
        if brother(x, y):
            print(x, "is brother of", y)
        if sister(x, y):
            print(x, "is sister of", y)
        if uncle(x, y):
            print(x, "is uncle of", y)
        if aunt(x, y):
            print(x, "is aunt of", y)
        if nephew(x, y):
            print(x, "is nephew of", y)
        if niece(x, y):
            print(x, "is niece of", y)
        if cousin(x, y):
            print(x, "is cousin of", y)
