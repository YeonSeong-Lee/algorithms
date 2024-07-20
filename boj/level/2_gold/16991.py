import sys
import math

input = sys.stdin.readline

n = int(input())
coordinate = []
VISITED = 1 << n
dp = [[-1] * VISITED for _ in range(n)]
dp[0][1] = 0
weight = [[0.0] * n for _ in range(n)]
for _ in range(n):
    x, y = list(map(int, input().split()))
    coordinate.append((x, y))


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


for i in range(n):
    for j in range(i + 1, n):
        if i != j:
            weight[i][j] = weight[j][i] = dist(coordinate[i], coordinate[j])
for bitmask in range(2, VISITED):
    visited = [i for i in range(n) if bitmask & (1 << i)]

    for cur in visited:
        temp = bitmask ^ (1 << cur)
        for prev in range(n):
            if dp[prev][temp] == -1 or weight[prev][cur] == 0:
                continue
            new_dist = dp[prev][temp] + weight[prev][cur]
            if dp[cur][bitmask] == -1:
                dp[cur][bitmask] = new_dist
            else:
                dp[cur][bitmask] = min(dp[cur][bitmask], new_dist)

mi = sys.maxsize

for i in range(n):
    if dp[i][VISITED - 1] == -1 or weight[i][0] == 0:
        continue
    mi = min(mi, dp[i][VISITED - 1] + weight[i][0])


print(mi)
