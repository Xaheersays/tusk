# Bellman Ford Algorithm:

# Single src shortest path:

# Difference between this and dijkstra's algo is that this can support -ve weights assigned to edges. 



# Pre-requisites:
# 	cycles with total path sum as -ve is not allowed


# Reasoning:

# 1. if src and destination are same then dist is 0. dist[x][x] is always 0 . that means even though we dont know anything about the distance from Src we we know that 
	
# 	Dist[Src] = 0 which is its absolute shortest distance. 

# 	for all other nodes X we have dist[X] = infinity

# 2. Relaxation Process:
	
# 	if dist[x] = dx & dis[y] = dy and we discover edge[x][y] = p such that 
	
# 	dy > dx + p 

# 	then we can say dist[y] = dx + p . or we can say

#     dist[y] = min(dist[y], dist[x] + edge[x][y]) for all nodes x which have an edge to y


# 3. if we relax all edges and there is a change in some vertice's distance then that change can trigger other changes and we have to redo relaxation for all the nodes again.
# if distance does not change we can be certain that this is the shortest path for all nodes.

# 4. Max number of times all edges need to be relaxed is n-1 where n is the number of nodes.
	
# 	proof:
# 		relaxation starts from src
		
# 		the longest path that can be from src to any node (no cycles included) can be of n-1 edges.

# 		and every time atleast on of the edge in this path would get updated (if needed)

# 		so max n - 1 iterations of the relaxation process are required


# algo:

# for n-1 times:
# 	any_edge_updated = False
# 	for all edges:
# 		if dist[edge.dest] > edge.wt + dist[edge.src]:
# 			dist[edge.dest] = edge.wt + dist[edge.src]
# 			any_edge_updated = True
# 	if not any_edge_updated:
# 		break

# // note that the above code will not update anything if dist[edge.src] is infinity

# code :

adj = [[None, 5, 2, None, None],
       [None, None, 1, None, None],
       [None, None, None, -1, -1],
       [None, None, None, None, None],
       [3, None, None, 2, None]]

inf = 999999999999999
n = len(adj)
src = 0
dist = [inf] * n
dist[src] = 0

for _ in range(n - 1):
    any_edge_updated = False
    for nodefrom in range(n):
        for nodeto in range(n):
            if adj[nodefrom][nodeto] and dist[nodefrom] != inf and dist[nodeto] > adj[nodefrom][nodeto] + dist[nodefrom]:
                dist[nodeto] = adj[nodefrom][nodeto] + dist[nodefrom]
                any_edge_updated = True
        if not any_edge_updated:
            break

print(dist)

# output:
# [0, 5, 2, 1, 1]


# time complexity:
# 	e*v

# 	if v is n and we know e is at max v*v-1

# 	=> O(n^3)
