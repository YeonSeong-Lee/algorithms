import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
stack = deque()
ans = [-1] * n
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)
