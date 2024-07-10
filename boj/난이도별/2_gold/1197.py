import sys
input = sys.stdin.readline

v, e = map(int, input().split())
root = [i for i in range(v+1)]
rank = [0 for _ in range(v+1)]
edges = []
def get_root(x):
  if root[x] == x:
    return x
  else:
    root[x] = get_root(root[x])
    return root[x]

def union(x, y):
  x = get_root(x)
  y = get_root(y)
  if x == y:
    return
  if rank[x] > rank[y]:
    root[y] = x
  else:
    root[x] = y
    if rank[x] == rank[y]:
      rank[x] += 1
  
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

ans = 0
for a, b, c in edges:
  if get_root(a) == get_root(b):
    continue
  union(a, b)
  ans += c

print(ans)

