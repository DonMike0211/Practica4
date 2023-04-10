import heapq

def prim(graph, start):
    mst = set()
    visited = set([start])
    edges = [
        (cost, start, end)
        for end, cost in graph[start].items()
    ]
    heapq.heapify(edges)
    while edges:
        cost, start, end = heapq.heappop(edges)
        if end not in visited:
            visited.add(end)
            mst.add((start, end, cost))
            for neighbor, neighbor_cost in graph[end].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_cost, end, neighbor))
    return mst

# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

mst = prim(graph, 'A')
print(mst) # Output: {('A', 'B', 2), ('B', 'C', 1), ('D', 'B', 1)}

