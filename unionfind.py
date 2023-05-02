class UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n+10)]
        self.rank =[1]*(n+10)
    def Find(self,n):
        if n==self.par[n]:
            return self.par[n]
        self.par[n] = self.Find(self.par[n])
        return self.par[n]
    def Union(self,n1,n2):
        p1 = self.Find(n1)
        p2 = self.Find(n2)
        if p1==p2:
            return 0
        if self.rank[p1]>=self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.rank[p2]+=self.rank[p1]
            self.par[p1] =  p2
        return 1

ip = [ ]
nodes = int(input())
for _ in range(nodes):
    e = [input(),input()]
    ip.append(nodes)
uf = UnionFind(n)
for u,v in ip:
    r= uf.Union(u,v)
