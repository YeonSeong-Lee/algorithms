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

# two pointer solution
# 투포인터를 사용할 때, 일단 이중 for문 돌면서 관찰해보기.