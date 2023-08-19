class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        parent = [i for i in range(n)]
        sizes = [1 for i in range(n)]
        
        def Union(p, q):
            p_ = find(p)
            q_ = find(q)
            if p_ == q_:
                return False
            if sizes[p_] < sizes[q_]:
                p_, q_ = q_, p_
            sizes[p_] += sizes[q_]
            parent[q_] = p_
            return True
        
        def find(p):
            while p != parent[p]:
                p = parent[p]
                parent[p] = parent[parent[p]]
            return p
        
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                if find(node) == find(neighbor):
                    return False
                Union(graph[node][0], neighbor)
                
        return True