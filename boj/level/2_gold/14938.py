import sys
from collections import defaultdict
input = sys.stdin.readline
n, m, r = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dist = [[sys.maxsize] * (n + 1) for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for i in range(1, n+1):
    temp = 0
    for idx, e in enumerate(dist[i]):
        if e <= m:
            temp += nums[idx]
    ans = max(temp, ans)

print(ans)
