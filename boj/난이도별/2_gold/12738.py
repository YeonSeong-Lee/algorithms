import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
lis = [nums[0]]

def bi_search(lis, target):
  left, right = 0, len(lis) - 1
  while left <= right:
    mid = (left + right) // 2
    if lis[mid] == target:
      return mid
    if lis[mid] < target:
      left = mid + 1
    if lis[mid] > target:
      right = mid - 1
  return left

for e in nums:
  if e > lis[-1]:
    lis.append(e)
  else:
    idx = bi_search(lis, e)
    lis[idx] = e

print(len(lis))
