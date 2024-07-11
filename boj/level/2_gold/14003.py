import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ids = [0 for _ in range(n)]
ids[0] = 1
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

for i, e in enumerate(nums):
  if e > lis[-1]:
    lis.append(e)
    ids[i] = len(lis)
  else:
    idx = bi_search(lis, e)
    lis[idx] = e
    ids[i] = idx + 1

max_len = len(lis)
print(max_len)
stack = deque()

for i in range(n-1, -1, -1):
  if max_len <= 0:
    break
  if max_len == ids[i]:
    max_len -= 1
    stack.append(nums[i])

while stack:
  print(stack.pop(), end=' ')