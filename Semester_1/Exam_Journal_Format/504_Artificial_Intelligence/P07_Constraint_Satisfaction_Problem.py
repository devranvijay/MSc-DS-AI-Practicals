# ------------------------------------------------------
# Practical No: 7
# Aim: To solve the Map Coloring problem as a Constraint Satisfaction
#      Problem (CSP) using backtracking in Python.
# ------------------------------------------------------

# Theory:
# A Constraint Satisfaction Problem consists of variables, domains
# (possible values) and constraints between variables. In map
# coloring, each region is a variable, the colors are the domain, and
# the constraint is that two neighboring regions must not have the
# same color. Backtracking search tries a color for a region and goes
# back if it creates a conflict.

# Algorithm:
# 1. Start
# 2. Take the regions with their neighbors, and the available colors
# 3. Assign a color to a region such that no neighboring region has
#    the same color
# 4. Move to the next region and repeat
# 5. If a region cannot be colored, backtrack and try a different color
# 6. When all regions are colored, print the solution
# 7. Stop

# Python Program:

neighbours = {
    'Region1': ['Region2', 'Region3'],
    'Region2': ['Region1', 'Region3', 'Region4'],
    'Region3': ['Region1', 'Region2', 'Region4'],
    'Region4': ['Region2', 'Region3'],
}

colors = ['Red', 'Green', 'Blue']
assigned = {}


def is_safe(region, color):

    for neighbour in neighbours[region]:
        if assigned.get(neighbour) == color:
            return False

    return True


def solve(regions):

    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            assigned[region] = color

            if solve(regions[1:]):
                return True

            del assigned[region]

    return False


region_list = list(neighbours.keys())

if solve(region_list):
    print("Solution found:")
    for region in region_list:
        print(region, "->", assigned[region])
else:
    print("No solution exists")

# Sample Input / Output:
# Solution found:
# Region1 -> Red
# Region2 -> Green
# Region3 -> Blue
# Region4 -> Red

# Result:
# The program to solve the Map Coloring CSP using backtracking was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What are the three components of a CSP?
# 2. What is the constraint in the Map Coloring problem?
# 3. What is backtracking search?
# 4. What is the minimum number of colors needed for any map (Four
#    Color Theorem)?
# 5. Give another real-life example of a CSP.
