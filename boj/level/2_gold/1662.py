import sys
from collections import deque

input = sys.stdin.readline


s = input().strip()
stack = deque()
result = 0
repeat = 0

for c in s:
    if c == "(":
        stack.append((result - 1, repeat))
        result = 0
    elif c == ")":
        prev_result, repeat = stack.pop()
        result = prev_result + result * repeat
    else:
        result += 1
        repeat = int(c)

print(result)
