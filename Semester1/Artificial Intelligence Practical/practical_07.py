variables = ['A', 'B', 'C', 'D']
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue'],
    'D': ['Red', 'Green', 'Blue']
}
constraints = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]
def is_valid(variable, color, assignment):
    for x, y in constraints:
        if x == variable and y in assignment:
            if assignment[y] == color:
                return False
        if y == variable and x in assignment:
            if assignment[x] == color:
                return False
    return True
def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    variable = next(v for v in variables if v not in assignment)
    for color in domains[variable]:
        if is_valid(variable, color, assignment):
            assignment[variable] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[variable]
    return None
solution = backtrack({})
print("Solution:")
print(solution)
