import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

dom_judge = defaultdict(int)
visited = defaultdict(int)

for _ in range(n):
    line = input().strip()
    visited[line] = 0
    dom_judge[line] += 1

cnt = 0

for _ in range(n):
    temp = input().strip()
    if visited[temp] < dom_judge[temp]:
        cnt += 1
        visited[temp] += 1
print(cnt)
