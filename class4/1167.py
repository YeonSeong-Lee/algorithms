import sys
from collections import defaultdict, deque
input = sys.stdin.readline

graph = defaultdict(list)
leaf = []
v = int(input().rstrip())

for i in range(v):
    s = list(map(int, input().split()))
    idx = s[0]
    for j in range(1, len(s)-1, 2):
        to, w = s[j], s[j+1]
        graph[idx].append((to, w))


def dfs(start):
    dist = [-1 for _ in range(v+1)]
    dist[start] = 0
    q = deque([start])

    while q:
        cur_node = q.pop()
        for n_n, n_w in graph[cur_node]:
            if dist[n_n] >= 0:
                continue
            dist[n_n] = dist[cur_node] + n_w
            q.append(n_n)
    return max(dist), dist.index(max(dist))

max_node = dfs(1)[1]
print(dfs(max_node)[0])