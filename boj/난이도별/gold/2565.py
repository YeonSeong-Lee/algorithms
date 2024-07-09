import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
wire = {}
for _ in range(n):
    a, b = map(int, input().split())
    wire[a] = b

nums = list(dict(sorted(wire.items())).values())
lis = [nums[0]]

for e in nums:
    if e > lis[-1]:
        lis.append(e)
    else:
        idx = bisect_left(lis, e)
        lis[idx] = e

print(n - len(lis))