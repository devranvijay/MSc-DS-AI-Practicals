# ===== 1a. Depth First Search (DFS) =====
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs(start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            # Add neighbors to stack in reverse order
            # to explore them in left-to-right order
            stack.extend(reversed(graph[vertex]))
# Run the DFS algorithm starting from node 'A'
dfs('A')
