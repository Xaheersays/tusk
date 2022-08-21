from collections import deque
def create_dir_adj(edges):
  numOfNodes=1+max([e[1]for e in edges]+[e[0]for e in edges])
  adj=[[0]*numOfNodes for _ in range(numOfNodes)]
  for e in edges:
    adj[e[0]][e[1]]=1
  return adj

def create_undir_adj(edges):
  numOfNodes=1+max([e[1]for e in edges]+[e[0]for e in edges])
  adj=[[0]*numOfNodes for _ in range(numOfNodes)]
  for e in edges:
    adj[e[0]][e[1]]=adj[e[1]][e[0]]=1
  return adj

def bfs(adj):
  vis=set()
  n=len(adj)
  for i in range(n):
    if i in vis:
      continue
    vis.add(i)
    q=deque([i])
    while q:
      ele=q.pop()
      print(ele,end=' ')
      for adjele in range(n):
        if adj[ele][adjele] and adjele not in vis:
          vis.add(adjele)
          q.appendleft(adjele)
  print()

def dfs(adj):
  vis=set()
  n=len(adj)
  for i in range(n):
    if i in vis:
      continue
    vis.add(i)
    st=deque([i])
    while st :
      ele=st.pop()
      print(ele,end='')
      for adjele in range(n):
        if adj[ele][adjele] and adjele not in vis:
          vis.add(adjele)
          st.append(adjele)
  print()
  
edges=[[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]]
adj_dir=create_dir_adj(edges)
adj_undir=create_undir_adj(edges)
for x in adj_dir:
  print(x)
print()
for x in adj_undir:
  print(x)

print()
print("bfs for dir")
bfs(adj_dir)
print()

print("bfs for undir")
bfs(adj_undir)
print()

print("dfs for dir")
dfs(adj_dir)
print()

print("dfs for undir")
dfs(adj_undir)

