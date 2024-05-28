import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
visited = [[-1] * 1001 for _ in range(1001)] 
q = deque()

for _ in range(1, n + 1):
    line = list(map(int, input().split()))
    for i, e in enumerate(line):
        if e == 2:
            q.append((_, i + 1))
            visited[_][i + 1] = 0
    info.append(line)


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if info[i - 1][j - 1] == 0:
            visited[i][j] = 0


dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    y, x = q.popleft()
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if ny > n or ny < 1 or nx > m or nx <  1:
            continue
        if visited[ny][nx] >= 0:
            continue
        q.append((ny, nx))
        visited[ny][nx] = visited[y][x] + 1



for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(visited[i][j], end=' ')
    print()