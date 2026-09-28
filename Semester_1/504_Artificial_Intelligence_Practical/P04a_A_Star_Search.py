# ------------------------------------------------------
# Practical No: 4 (a)
# Aim: To implement the A* search algorithm to find the shortest
#      path between two nodes in Python.
# ------------------------------------------------------

# Theory:
# A* search finds the shortest path using both the actual cost from
# the start node (g) and an estimated cost to the goal (heuristic, h).
# It always expands the node with the lowest value of f = g + h, which
# makes it faster than blind search methods while still finding the
# optimal path.

# Algorithm:
# 1. Start
# 2. Keep an open list of nodes to explore, starting with the start node
# 3. Pick the node from the open list with the lowest f = g + h value
# 4. If it is the goal node, stop and trace back the path using parent links
# 5. Otherwise move it to the closed list and update the cost of its
#    neighbours
# 6. Repeat until the goal is found
# 7. Stop

# Python Program:

graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3)],
    'D': [('G', 2)],
    'G': [],
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 4,
    'D': 1,
    'G': 0,
}


def a_star(graph, heuristic, start, goal):

    open_list = {start: heuristic[start]}
    closed_list = set()

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        current = min(open_list, key=open_list.get)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        del open_list[current]
        closed_list.add(current)

        for neighbour, cost in graph[current]:

            if neighbour in closed_list:
                continue

            new_cost = g_cost[current] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:

                g_cost[neighbour] = new_cost
                f_cost = new_cost + heuristic[neighbour]

                open_list[neighbour] = f_cost
                parent[neighbour] = current

    return None, None


path, cost = a_star(graph, heuristic, 'S', 'G')

print("Shortest Path :", " -> ".join(path))
print("Total Cost    :", cost)

# Sample Input / Output:
# Shortest Path : S -> A -> C -> D -> G
# Total Cost    : 7

# Result:
# The program to implement the A* search algorithm was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What does f = g + h represent in A* search?
# 2. What is a heuristic function?
# 3. What is an admissible heuristic?
# 4. Why is A* considered better than plain BFS for weighted graphs?
# 5. Name one real-world application of the A* algorithm.
