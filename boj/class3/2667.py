import sys
from collections import deque
input = sys.stdin.readline


def bfs(i,j):
    cnt = 0
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        cnt += 1
        y, x = q.popleft()
        for v in dir:
            dy, dx = v
            ny, nx = y + dy, x + dx
            if (ny >= n or nx >= n or ny < 0 or nx < 0):
                continue
            if visited[ny][nx] == 1:
                continue
            if info[ny][nx] == '0':
                continue
            q.append((ny,nx))
            visited[ny][nx] = 1
    return cnt

n = int(input())
dir = [(1,0), (0,1), (-1,0), (0,-1)]
visited = [[0] * n for _ in range(n)]
info = []
ans = []

for _ in range(n):
    line = input().strip()
    info.append(line)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 1 or info[i][j] == '0':
            continue
        ans.append(bfs(i,j))

print(len(ans))
ans.sort()
for e in ans:
    print(e)
