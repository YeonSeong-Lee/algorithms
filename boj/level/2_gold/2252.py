import sys
from collections import defaultdict

input = sys.stdin.readline
graph = defaultdict(list)

n, m = map(int, input().split())
visited = [0 for _ in range(n + 1)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(v):
    visited[v] = 1
    for e in graph[v]:
        if visited[e] == 1:
            continue
        visited[e] = 1
        dfs(e)
    ans.append(v)


for i in range(1, n + 1):
    if visited[i] == 1:
        continue
    dfs(i)

print(*ans[::-1])
