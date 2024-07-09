import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input().strip())
graph = defaultdict(list)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

def bfs(start):
  global n
  q = deque([start])
  dist = [-1 for _ in range(n+1)]
  dist[start] = 0
  while q:
    cur = q.popleft()
    for nc, nw in graph[cur]:
      if dist[nc] != -1:
        continue
      q.append(nc)
      dist[nc] = dist[cur] + nw
  ma = max(dist)
  return ma, dist.index(ma)

_, leaf = bfs(1)
print(bfs(leaf)[0])