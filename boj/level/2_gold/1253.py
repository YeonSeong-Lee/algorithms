import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0

for i in range(n):
  l, r = 0, n-1
  while l < r:
    if l == i:
      l += 1
      continue
    if r == i:
      r -= 1
      continue
    cur_sum = nums[l] + nums[r]
    if cur_sum == nums[i]:
      ans += 1
      break
    if cur_sum < nums[i]:
      l += 1
    else:
      r -= 1

print(ans)