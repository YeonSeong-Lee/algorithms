from collections import deque
import sys
input = sys.stdin.readline
cows = []
stack = deque()

n = int(input())
for _ in range(n):
    cows.append(int(input()))
cows.append(sys.maxsize)

ans = 0

for e in cows:
    while stack and stack[-1] <= e:
        stack.pop()
    ans += len(stack)
    stack.append(e)
print(ans) 

# LEARN
# 어떤 수를 셀 때는 기준을 바꾸어서 셀 수 있는지 생각해보기.