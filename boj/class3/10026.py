import sys
from collections import deque

input = sys.stdin.readline

h_visited = [[-1] * 101 for _ in range(101)] 
h_ans = 0
c_ans = 0
c_visited = [[-1] * 101 for _ in range(101)] 
info = []
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n = int(input())

def bfs(i, j, visited):
    q = deque()
    q.append((i, j, info[i-1][j-1]))
    visited[i][j] = 1
    while q:
        y, x, c = q.popleft()
        for d in dir:
            dy, dx = d
            ny, nx = y + dy, x + dx
            if (ny < 1 or ny > n or nx < 1 or nx > n):
                continue
            if info[ny-1][nx-1] != c or visited[ny][nx] == 1:
                continue
            q.append((ny, nx, c))
            visited[ny][nx] = 1

for _ in range(n):
    line = input().strip()
    info.append(line)

for i in range(1, n+1):
    for j in range(1, n+1):
        if h_visited[i][j] == 1:
            continue
        h_ans += 1
        bfs(i, j, h_visited)

for i, line in enumerate(info):
    info[i] = line.replace("R", "G")

for i in range(1, n+1):
    for j in range(1, n+1):
        if c_visited[i][j] == 1:
            continue
        c_ans += 1
        bfs(i, j, c_visited)

print(h_ans, c_ans)
