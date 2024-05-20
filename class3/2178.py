import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
visited = [[False] * 100 for _ in range(100)]

for _ in range(n):
    v = input()
    info.append(v)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
q.append((1, 1))
visited[1][1] = True
cnt = 1
while q:
    y, x = q.popleft()
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if (nx < 1 or nx > m or ny < 1 or ny > n):
            continue
        if (info[ny - 1][nx - 1] == 0):
            continue
        if (visited[ny][nx] == True):
            continue
        if (nx == m - 1 or ny == n - 1):
            continue
        q.append((ny, nx))
        visited[ny][nx] = True
        cnt += 1

print(cnt)
        


