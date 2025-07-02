def dfs(graph):
    visited = {n: False for n in graph}
    predecessor = {n: None for n in graph}
    discovery_time = {n: 0 for n in graph}
    finish_time = {n: 0 for n in graph}
    time = 0

    def dfs_visit(u):
        nonlocal time
        time += 1
        discovery_time[u] = time
        visited[u] = True
        print(f"Visiting node: {u} at time {time}")
        for v in graph[u]:
            if not visited[v]:
                predecessor[v] = u
                dfs_visit(v)
        time += 1
        finish_time[u] = time
        print(f"Finishing node: {u} at time {time}")

    for node in graph:
        if not visited[node]:
            dfs_visit(node)

    return {
        "discovery": discovery_time,
        "finish": finish_time,
        "predecessor": predecessor
    }


# Example graph (adjacency list representation)
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS on the example graph
result = dfs(example_graph)

# Print the results
print("\nFinal Results:")
print("Discovery times:", result["discovery"])
print("Finish times:", result["finish"])
print("Predecessors:", result["predecessor"])