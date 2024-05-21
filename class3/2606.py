import sys
input = sys.stdin.readline
from collections import deque

compute_cnt = int(input())
n = int(input())
graph = [deque() for _ in range(101)]
visited = [0 for _ in range(101)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visited[1] = 1
cnt = 0

while q:
    cur = q.popleft()
    while len(graph[cur]) != 0:
        temp = graph[cur].popleft()
        if (visited[temp] == 1):
            continue
        visited[temp] = 1
        q.append(temp)
        cnt += 1

print(cnt)




