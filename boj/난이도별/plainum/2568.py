import sys
input = sys.stdin.readline
from collections import deque
from bisect import bisect_left

n = int(input())
wire = {}
for _ in range(n):
    a, b = map(int, input().split())
    wire[b] = a

nums = list(dict(sorted(wire.items())).values())
lis = [nums[0]]
ids = [0 for _ in range(n)]

for i, e in enumerate(nums):
    if e > lis[-1]:
        lis.append(e)
        ids[i] = len(lis)
    else:
        idx = bisect_left(lis, e)
        lis[idx] = e
        ids[i] = idx + 1

lis_num = len(lis)
stack = deque()

for i in range(n-1, -1, -1):
    if ids[i] == lis_num:
        lis_num -= 1
        stack.append(nums[i])
    if lis_num <= 0:
        break


# 없애야하는 전깃줄 최소값
print(n - len(lis))
# 없애야하는 A전봇대 연결위치

need_to_deleted = []

for e in nums:
    if e not in stack:
        need_to_deleted.append(e)

need_to_deleted.sort()

for e in need_to_deleted:
    print(e)