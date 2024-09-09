from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
circles = []

for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, x))
    circles.append((x+r, x))

circles.sort()
stack = deque()

for e in circles:
    if stack:
        if stack[-1][1] == e[1]:
            stack.pop()
        else:
            stack.append(e)
    else:
        stack.append(e)

print("YES") if not stack else print("NO")

# LEARN
# 적절한 괄호쌍 문제로 환원하기, 데이터값들 정렬해서 넣기