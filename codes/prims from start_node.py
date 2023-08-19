import heapq

def prim(graph):
    num_vertices = len(graph)
    mst = []  # List to store the edges of the minimum spanning tree
    visited = [False] * num_vertices
    start_node = 0
    heap = [(0, start_node)]  # Priority queue to store (weight, vertex) pairs

    while heap:
        weight, vertex = heapq.heappop(heap)  # Get the edge with the smallest weight
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        if vertex != 0:  # Skip the first iteration since it doesn't have an edge
            mst.append((vertex, parent[vertex], weight))  # Add the edge to the MST

        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(heap, (edge_weight, neighbor))
                parent[neighbor] = vertex  # Track the parent vertex for each neighbor

    return mst

# Example graph represented as an adjacency list of (neighbor, weight) pairs
graph = {
    0: [(1, 2), (3, 4)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 5)],
    3: [(0, 4), (1, 8), (2, 5)]
}

parent = [-1] * len(graph)  # To track the parent vertex for each vertex

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for vertex, parent_vertex, weight in minimum_spanning_tree:
    print(f"Edge: ({parent_vertex} - {vertex}), Weight: {weight}")
