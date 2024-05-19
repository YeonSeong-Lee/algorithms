import sys
input = sys.stdin.readline
from collections import deque


def dfs(start):
    visited2[start] = 1
    print(start, end = ' ')
    for i in range(1, N + 1):
        if (visited2[i] == 0 and graph[start][i] == 1):
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1, N + 1):
            if (visited[i] == 0 and graph[v][i] == 1):
                q.append(i)
                visited[i] = 1
             


N, M, start = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
visited2 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(start)
print()
bfs(start)