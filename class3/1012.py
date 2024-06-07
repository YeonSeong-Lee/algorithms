import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(i, j):
    dir = [(1,0), (-1,0), (0, 1), (0,-1)]
    q = deque()
    q.append((i,j))
    while q:
        y, x = q.popleft()
        for d in dir:
            dy, dx = d
            ny, nx = y + dy, x + dx
            if (nx < 0 or ny < 0 or nx >= m or ny >= n):
                continue
            if info[ny][nx] == 0 or visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            q.append((ny, nx))

for _ in range(t):
    m, n, k = map(int, input().split())
    info = [[0] * 50 for _ in range(50)]
    visited = [[0] * 50 for _ in range(50)]
    ans = 0
    for _ in range(k):
        x, y = map(int, input().split())
        info[y][x] = 1
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1 or info[i][j] == 0:
                continue
            ans += 1
            bfs(i,j)
    print(ans)