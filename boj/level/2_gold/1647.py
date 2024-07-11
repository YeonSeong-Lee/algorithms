import sys
input = sys.stdin.readline

n, m = map(int, input().split())
root = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
edges = []

def find(x):
  if root[x] == x:
    return x
  else:
    root[x] = find(root[x])
    return root[x]

def union(a, b):
  x = find(a)
  y = find(b)
  if rank[x] < rank[y]:
    root[x] = y
  else:
    root[y] = x
    if rank[x] == rank[y]:
      rank[x] += 1


for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

ans = 0
last = 0
for a, b, c in edges:
  if find(a) == find(b):
    continue
  union(a, b)
  ans += c
  last = c

print(ans - last)