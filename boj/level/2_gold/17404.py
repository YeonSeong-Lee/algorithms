import sys
input = sys.stdin.readline

n = int(input())
colors = []
for _ in range(n):
  r, g, b = map(int, input().split())
  colors.append((r,g,b))

ans = 1e9
for i in range(3):
  dp = [[1e9] * 3 for _ in range(n)]
  dp[0][i] = colors[0][i]
  for j in range(1, n):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + colors[j][0]
    dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + colors[j][1]
    dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + colors[j][2]
  dp[-1][i] = 1e9
  ans = min(ans, min(dp[-1]))

print(ans)