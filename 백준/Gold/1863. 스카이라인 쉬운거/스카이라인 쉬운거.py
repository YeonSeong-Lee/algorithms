from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

stack = deque()
ans = 0
for _ in range(n + 1):
    if _ == n:
        x, y = 0, 0
    else:
        x, y = map(int, input().split())
    h = y
    while stack and stack[-1] > y:
        if stack[-1] != h:
            ans += 1
            h = stack[-1]
        stack.pop()
    stack.append(y)

print(ans)
