import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
  nums.append(int(input().strip()))

nums.sort()
ans = nums[-1] - nums[0]

for i in range(n):
  l = bisect_left(nums, nums[i] + m)
  if l < n:
    ans = min(ans, nums[l] - nums[i])

print(ans)
