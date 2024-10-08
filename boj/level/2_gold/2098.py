import sys

input = sys.stdin.readline

n = int(input())
weight = []
VISITED = 1 << n
dp = [[sys.maxsize] * VISITED for _ in range(n)]
dp[0][1] = 0
for _ in range(n):
    line = list(map(int, input().split()))
    weight.append(line)

for bitmask in range(2, VISITED):
    visited = [i for i in range(n) if bitmask & (1 << i)]

    for cur in visited:
        temp = bitmask ^ (1 << cur)
        for prev in range(n):
            if dp[prev][temp] == -1 or weight[prev][cur] == 0:
                continue
            new_dist = dp[prev][temp] + weight[prev][cur]
            dp[cur][bitmask] = min(dp[cur][bitmask], new_dist)

mi = sys.maxsize

for i in range(n):
    if dp[i][VISITED - 1] == -1 or weight[i][0] == 0:
        continue
    mi = min(mi, dp[i][VISITED - 1] + weight[i][0])


print(mi)
