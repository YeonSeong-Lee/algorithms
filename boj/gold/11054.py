import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
increase_dp = [1 for _ in range(n)]
decrease_dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if nums[i] > nums[j]:
      increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)


for i in range(n-1, -1, -1):
  for j in range(i, n):
    if nums[i] > nums[j]:
      decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

print(max(list(map(lambda x: x[0] + x[1], zip(increase_dp, decrease_dp))))-1)