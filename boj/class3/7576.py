import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
info = []
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
ans = 0

for _ in range(n):
    line = list(map(int, input().split()))
    for i, e in enumerate(line):
        if e == 1:
            q.append((_, i))
            visited[_][i] = 0
    info.append(line)

while q:
    y, x = q.popleft()
    for d in dir:
        dy, dx = d
        ny, nx = y + dy, x + dx
        if (ny >= n or nx >= m or ny < 0 or nx < 0):
            continue
        if info[ny][nx] == -1:
            continue
        if visited[ny][nx] >= 0:
            continue
        visited[ny][nx] = visited[y][x] + 1
        ans = max(ans, visited[ny][nx])
        q.append((ny, nx))

impossible_flag = False
for i in range(n):
    for j in range(m):
        if visited[i][j] >= 0:
            continue
        if info[i][j] == -1:
            continue
        impossible_flag = True

print(ans if impossible_flag == False else -1)