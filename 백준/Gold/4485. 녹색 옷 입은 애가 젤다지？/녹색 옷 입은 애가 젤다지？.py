import heapq
import sys
input = sys.stdin.readline

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(grid, n):
    dist = [[sys.maxsize] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    q = [(grid[0][0], 0, 0)]

    while q:
        cost, y, x = heapq.heappop(q)
        if cost > dist[y][x]:
            continue

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            nc = cost + grid[ny][nx]
            if nc < dist[ny][nx]:
                dist[ny][nx] = nc
                heapq.heappush(q, (nc, ny, nx))

    return dist[n-1][n-1]


i = 1
while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    print(f"Problem {i}: {dijkstra(grid, n)}")
    i += 1
