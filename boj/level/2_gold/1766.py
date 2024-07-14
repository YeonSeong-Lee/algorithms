import sys

from collections import defaultdict
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = []
res = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    res.append(cur)
    for i in graph[cur]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(q, i)

print(*res)
