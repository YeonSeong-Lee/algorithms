import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [deque() for _ in range(1001)]
visited = [0] * 1001
ans = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        cur = q.popleft()
        while graph[cur]:
            e = graph[cur].popleft()
            if visited[e] == 1:
                continue
            visited[e] = 1
            q.append(e)

for i in range(1, n+1):
    if visited[i] == 1:
        continue
    bfs(i)
    ans += 1

print(ans-1)