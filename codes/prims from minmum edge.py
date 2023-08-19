import heapq

def prim_start_from_minimum(graph):
    num_vertices = len(graph)
    mst = []  # List to store the edges of the minimum spanning tree
    visited = [False] * num_vertices
    heap = []  # Priority queue to store (weight, vertex) pairs

    # Find the minimum-weight edge to start with
    for vertex, edges in graph.items():
        for neighbor, weight in edges:
            heapq.heappush(heap, (weight, vertex, neighbor))

    # Add the minimum-weight edge to the MST and mark its vertices as visited
    weight, vertex, neighbor = heapq.heappop(heap)
    visited[vertex] = True
    visited[neighbor] = True
    mst.append((vertex, neighbor, weight))

    while heap:
        weight, vertex, neighbor = heapq.heappop(heap)
        if visited[vertex] and not visited[neighbor]:
            visited[neighbor] = True
            mst.append((vertex, neighbor, weight))

        for next_neighbor, next_weight in graph[neighbor]:
            if not visited[next_neighbor]:
                heapq.heappush(heap, (next_weight, neighbor, next_neighbor))

    return mst

# Example graph represented as an adjacency list of (neighbor, weight) pairs
graph = {
    0: [(1, 2), (3, 4)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 5)],
    3: [(0, 4), (1, 8), (2, 5)]
}

minimum_spanning_tree = prim_start_from_minimum(graph)
print("Minimum Spanning Tree:")
for vertex, neighbor, weight in minimum_spanning_tree:
    print(f"Edge: ({vertex} - {neighbor}), Weight: {weight}")
