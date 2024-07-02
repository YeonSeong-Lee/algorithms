from collections import deque, defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0] * (n+1)
visited = [0] * (n+1)
q = deque([1])

while q:
  cur = q.popleft()
  for next in graph[cur]:
    if visited[next] != 0:
      continue
    parent[next] = cur
    visited[next] = 1
    q.append(next)

for i in range(2, n+1):
  print(parent[i])
