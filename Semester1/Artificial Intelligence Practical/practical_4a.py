# ===== 4a. A* Search Algorithm =====
import heapq
graph = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 16},
    'F': {'G': 16},
    'G': {}
}
h = {'S': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}
def a_star(start, goal):
    pq = [(h[start], 0, start, [])]
    while pq:
        f, g, node, path = heapq.heappop(pq)
        path = path + [node]
        if node == goal:
            return path, g
        for nbr, cost in graph[node].items():
            heapq.heappush(pq, (g + cost + h[nbr], g + cost, nbr, path))
path, cost = a_star('S', 'G')
print("Shortest path:", path)
print("Total cost:", cost)
