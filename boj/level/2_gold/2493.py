import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
heights = list(map(int, input().split()))

stack = []
result = [0] * n

for i in range(n):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(map(str, result)))

# LEARN
# LIFO를 보고 stack생각해야함.
# 스택으로 쓸모없는 정보를 지울 수 있음.