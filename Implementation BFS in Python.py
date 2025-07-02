from collections import deque

def bfs(graph, start):
    """
    Perform BFS; return distance and predecessor maps.
    """
    visited     = {n: False for n in graph}
    distance    = {n: float('inf') for n in graph}
    predecessor = {n: None for n in graph}

    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:  # <-- fixed indentation here
        u = queue.popleft()
        # print(f"Visiting node: {u}")  # optional logging

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)

    return {"distance": distance, "predecessor": predecessor}

# Example usage:
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = bfs(graph_example, 'A')
print("\nBFS Results:")
for node, dist in result["distance"].items():
    pred = result["predecessor"][node]
    print(f"Node {node}: Distance = {dist}, Predecessor = {pred}")