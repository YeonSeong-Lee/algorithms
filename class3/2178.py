import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
visited = [[0] * 101 for _ in range(101)]

for _ in range(n):
    v = input()
    info.append(v)  

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
q.append((1, 1))
visited[1][1] = 1
while q:
    y, x = q.popleft()
    if x == m and y == n:
        break
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if (nx < 1 or nx > m or ny < 1 or ny > n):
            continue
        if (info[ny - 1][nx - 1] == '0'):
            continue
        if (visited[ny][nx] >= 1):
            continue
        q.append((ny, nx))
        visited[ny][nx] = visited[y][x] + 1

print(visited[n][m])

