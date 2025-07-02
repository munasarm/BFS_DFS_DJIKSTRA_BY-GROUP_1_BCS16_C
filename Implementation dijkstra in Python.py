import heapq

def dijkstra(graph, start):
  
    distances = {n: float('inf') for n in graph}
    predecessors = {n: None for n in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > distances[u]:
            continue

        for v, weight in graph[u].items():
            new_dist = current_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                predecessors[v] = u
                heapq.heappush(priority_queue, (new_dist, v))

    return {"distances": distances, "predecessors": predecessors}

# Example graph (weighted adjacency list)
example_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run Dijkstra's algorithm from node 'A'
result = dijkstra(example_graph, 'A')

# Print results
print("Shortest distances from 'A':", result["distances"])
print("Predecessors in shortest paths:", result["predecessors"])