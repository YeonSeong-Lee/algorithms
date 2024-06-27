import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
info = []
sharks = [0, 0]
size = [2, 0]

def bfs(start):
    ans = 0
    q = []
    temp_y, temp_x = start
    visited = [[-1] * n for _ in range(n)]
    visited[temp_y][temp_x] = 0
    heapq.heappush(q, (visited[temp_y][temp_x], temp_y, temp_x))
    dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while q:
        dummy, y, x  = heapq.heappop(q)
        if info[y][x] < size[0] and info[y][x] > 0:
            size[1] += 1
            ans += visited[y][x]
            visited = [[-1] * n for _ in range(n)]
            visited[y][x] = 0
            q = []
            info[y][x] = 0
            if size[1] == size[0]:
                size[0] += 1
                size[1] = 0
        for v in dir:
            dy, dx = v
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or nx >= n or ny >= n:
                continue
            if visited[ny][nx] >= 0:
                continue
            if info[ny][nx] > size[0]:
                continue
            visited[ny][nx] = visited[y][x] + 1
            heapq.heappush(q, (visited[ny][nx], ny, nx))
    return ans


for _ in range(n):
    line = list(map(int, input().split()))
    for i, e in enumerate(line):
        if e == 9:
            sharks = (_, i)
            line[i] = 0
    info.append(line)

print(bfs(sharks))
