from collections import deque
def create_adj_mat(edges):
  numOfNodes=1+max([e[1]for e in edges]+[e[0] for e in edges])
  adj=[[0]*numOfNodes for _ in range(numOfNodes)]
  for e in edges:
    adj[e[0]][e[1]]=1
  return adj

def create_adj_undir_mat(edges):
  numOfNodes=1+max([e[1]for e in edges] + [e[0] for e in edges])
  adj=[[0]*numOfNodes for _ in range(numOfNodes)]
  for e in edges:
    adj[e[0]][e[1]]=adj[e[1]][e[0]]=1
  return adj

def bfs(adj):
  print("bfs")
  n=len(adj)
  vis=set()
  for i in range(n):
    if i in  vis:
      continue
    q=deque([i])
    vis.add(i)
    while q:
      ele=q.pop()
      print(ele,end=' ')
      for adjele in range(n):
        if adj[ele][adjele] and adjele not in vis:
          vis.add(adjele)
          q.appendleft(adjele)

  print()

def dfs(adj):
  print("dfs")
  vis=set()
  n=len(adj)
  for i in range(n):
    if i in vis:
      continue
    st=deque([i])
    vis.add(i)

    while st:
      ele=st.pop()
      print(ele,end=' ')
      for adjele in range(n):
        if adj[adjele][ele] and adjele not in vis :
          vis.add(adjele)
          st.append(adjele)
  print()

def detect_cycle_bfs(adj):
  vis=set()
  n=len(adj)
  for i in range(n):
    if i in vis:
      continue
    q=deque([[i,-1]])
    vis.add(i)
    while q:
      ele,par=q.pop()
      for adjele in range(n):
        if adj[adjele][ele]:
          if adjele not in vis:
            vis.add(adjele)
            q.appendleft([adjele,ele])
          elif adjele != par :
            print(f"cycle found at {ele}-{adjele}")
            return
  print()

def detect_cycle_dfs(adj):
  vis=set()
  n= len(adj)
  for i in range(n):
    if i in vis:
      continue
    st=deque([[i,-1]])
    vis.add(i)
    while st:
      ele,par=st.pop()
      for adjele in range(n):
        if adj[ele][adjele]:
          if adjele not in vis:
            vis.add(adjele)
            st.append([adjele,ele])
          elif adjele !=par :
            print(f"cycle found at {ele}-{adjele}")
            return
  print()

def dfs_recursive(adj,vis,ele,par):
  vis.add(ele)
  for adjele in range(len(adj)):
    if adj[ele][adjele]:
      if adjele not in vis:
        if dfs_recursive(adj,vis,adjele,ele):
          return True
      elif adjele!=par:
        print(f"cycle found at {ele} -{adjele}")
        return True
def detect_cycle_dfs_recursive(adj):
  vis=set()
  for i in range(len(adj)):
    if i in vis:
      continue
    if dfs_recursive(adj,vis,i,-1):
      return 
  print("no cycle found")

def dfs_recursive_path(adj,vis,path,ele):
  vis.add(ele)
  path.add(ele)
  for adjele in range(len(adj)):
    if adj[ele][adjele]:
      if adjele not in  vis:
        if dfs_recursive_path(adj,vis,path,adjele):
          return True
      elif adjele in  path:
        print(f"cycle found at {ele}-{adjele}")
        return True
  path.remove(ele)
  print()

def detect_cycle_dir(adj):
  vis=set()
  n=len(adj)
  for i in range(n):
    if i in vis:
      continue
    if dfs_recursive_path(adj,vis,set(),i):
      return
  print("no cycle found")
    
  
edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [5, 7], [7, 6],[6,6]]

adj_dir=create_adj_mat(edges)
adj_undir=create_adj_undir_mat(edges)
print()
print("adj dir mat")
for x in adj_dir:
  print(x)

print()
print("adj undir mat")
for x in adj_undir:
  print(x)
print()
bfs(adj_dir)
print()
dfs(adj_undir)

print()
print("cycle detection through bfs")
detect_cycle_bfs(adj_undir)

print()
print("cycle detection using dfs")
detect_cycle_dfs(adj_undir)
print()
print("cycle detection using recursive dfs")
detect_cycle_dfs_recursive(adj_undir)
print()
print("cycle detection in dir graph using recursive dfs ")
detect_cycle_dir(adj_dir)
