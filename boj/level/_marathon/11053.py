import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]
dp[1] = 1

for i in range(1, n+1):
  for j in range(1, i):
    if nums[i-1] > nums[j-1]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))