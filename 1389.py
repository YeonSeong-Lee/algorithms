import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N) for _ in range(N)]

for i in range(N):
  for j in range(N):
    if i == j:
      graph[i][j] = 0


for i in range(M):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      if k == i or k == j or i == j:
        continue
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = N
total = INF
for i, _ in enumerate(graph):
  if total > sum(_):
    total = sum(_)
    res = i + 1
print(res)
