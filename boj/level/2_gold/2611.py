import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)
dp = [0 for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
prev = [-1 for _ in range(n+1)]
path = []


for _ in range(m):
    p, q, r = map(int, input().split())
    in_degree[q] += 1
    graph[p].append((q, r))

q = deque([(1, 0)])

while q:
    cur = q.popleft()
    idx, score = cur
    for ni, ns in graph[idx]:
        in_degree[ni] -= 1
        if dp[ni] < dp[idx] + ns:
            dp[ni] = dp[idx] + ns
            prev[ni] = idx
        if in_degree[ni] == 0 and ni != 1:
            q.append((ni, ns))


print(dp[1])
path = []
node = 1
while node != -1:
    path.append(node)
    if prev[node] == 1:
        path.append(1)
        break
    node = prev[node]


print(*path[::-1])

# LEARN
# 위상정렬, 경로 기억하기