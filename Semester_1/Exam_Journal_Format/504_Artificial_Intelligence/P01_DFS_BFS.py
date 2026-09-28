# ------------------------------------------------------
# Practical No: 1
# Aim: To implement Depth First Search (DFS) and Breadth First
#      Search (BFS) traversal of a graph in Python.
# ------------------------------------------------------

# Theory:
# DFS explores as far as possible along each branch before
# backtracking, and is implemented using a stack. BFS explores all
# neighbors of a node before moving to the next level, and is
# implemented using a queue. Both are used to visit every node of a
# graph.

# Algorithm (DFS):
# 1. Start
# 2. Push the start node onto a stack
# 3. Pop a node, if not visited, mark it visited and print it
# 4. Push all its unvisited neighbors onto the stack
# 5. Repeat until the stack is empty
# 6. Stop

# Algorithm (BFS):
# 1. Start
# 2. Insert the start node into a queue
# 3. Remove a node from the front of the queue, mark it visited and print it
# 4. Insert all its unvisited neighbors into the queue
# 5. Repeat until the queue is empty
# 6. Stop

# Python Program:

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E'],
}


def dfs(graph, start):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited


def bfs(graph, start):

    visited = []
    queue = [start]

    while queue:

        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited


print("DFS Traversal :", dfs(graph, 'A'))
print("BFS Traversal :", bfs(graph, 'A'))

# Sample Input / Output:
# DFS Traversal : ['A', 'C', 'F', 'B', 'E', 'G', 'D']
# BFS Traversal : ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Result:
# The program to implement DFS and BFS traversal was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What data structure does DFS use? What about BFS?
# 2. Does BFS always find the shortest path? Why?
# 3. What is the time complexity of DFS and BFS?
# 4. Why do we maintain a visited list in graph traversal?
# 5. What is the difference between a tree and a graph?
