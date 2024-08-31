import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stacks = [deque() for _ in range(4)]

for e in nums:
    flag = False
    for s in stacks:
        if not s or (s and s[-1] < e):
            s.append(e)
            flag = True
            break
    if flag == False:
        print("NO")
        exit()

print("YES")

# 그리디 문제
