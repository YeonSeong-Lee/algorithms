import sys
import math
input = sys.stdin.readline

n  = int(input())
groups = [(0, 0, 0) for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    groups[i] = (x, 0, y)
    if i != 0:
        p = 1
        if y - groups[i-1][2] == 0:
            p = 0
        elif y - groups[i-1][2] < 0:
            p = -1
        groups[i - 1] = (groups[i-1][0], x, p)


q = int(input())
for _ in range(q):
    k = float(input())
    start = 0
    end = len(groups) - 1
    mid = (start + end) // 2

    while start <= end:
        mid = (start + end) // 2
        temp = groups[mid]
        if temp[0] < k < temp[1]:
            break
        if temp[0] > k:
            end = mid - 1
        if temp[0] < k:
            start = mid + 1
        
    print(groups[mid][2])
