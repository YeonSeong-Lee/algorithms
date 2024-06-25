import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = []
dp = [[0] * (k+1) for _ in range(n)]

for _ in range(n):
  w, v = map(int, input().split())
  item.append((w, v))

for weight in range(1, k+1):
  w, v = item[0]
  if weight >= w:
    dp[0][weight] = v

for item_idx in range(1, n):
  for weight in range(1, k+1):
    w, v = item[item_idx]
    if w > weight:
      dp[item_idx][weight] = dp[item_idx - 1][weight]
    else:
      dp[item_idx][weight] = max(dp[item_idx-1][weight], dp[item_idx - 1][weight-w] + v)

print(dp[n-1][k])