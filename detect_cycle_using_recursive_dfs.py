

def create_undir_adj(edges):
    numOfNodes = 1 + max([e[1] for e in edges] + [e[0] for e in edges])
    adj = [[0] * numOfNodes for _ in range(numOfNodes)]
    for e in edges:
        adj[e[0]][e[1]] = adj[e[1]][e[0]] = 1
    return adj


def dfs_recursive(adj,vis,ele,par):
    vis.add(ele)
    for adjele in range(len(adj)):
        if adj[ele][adjele]:
            if adjele not in vis:
                if dfs_recursive(adj,vis,adjele,ele):
                    return True
            elif adjele!=par:
                print(f"cycle found at {ele}-{adjele}")
                return True
    return False

def detect_cycle_undirected_dfs_recursive(adj):
    vis=set()
    n=len(adj)
    for i in range(n):
        if i in vis:
            continue
        if dfs_recursive(adj,vis,i,-1):
            return
    print("no cycle found")


edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [5, 7], [7, 6]]
adj_undir = create_undir_adj(edges)
print()
print("cycle detection using recursive dfs")
detect_cycle_undirected_dfs_recursive(adj_undir)
#output
# [0, 1, 0, 0, 0, 0, 0, 0]
# [1, 0, 1, 1, 0, 0, 0, 0]
# [0, 1, 0, 0, 1, 0, 0, 0]
# [0, 1, 0, 0, 1, 0, 0, 0]
# [0, 0, 1, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 1, 1, 0]
# cycle detection using recursive dfs
# cycle found at 3-1
