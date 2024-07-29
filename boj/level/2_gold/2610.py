import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
m = int(input())

root = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]


def find(idx):
    if root[idx] == idx:
        return idx
    else:
        root[idx] = find(root[idx])
        return root[idx]


def find_path(idx):
    q = deque([idx])
    path = [idx]
    while q:
        cur = q.popleft()
        for i in range(1, n+1):
            if dist[cur][i] == 0 or dist[cur][i] == sys.maxsize:
                continue
            if i in path:
                continue
            path.append(i)
            q.append(i)
    return path


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    if rank[x] < rank[y]:
        root[y] = x
    else:
        root[x] = y
        if rank[x] == rank[y]:
            rank[x] += 1
    return


dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0


visited = []
for i in range(1, n+1):
    x = find(i)
    if x not in visited:
        visited.append(x)
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

print(len(visited))
ans = []

for e in visited:
    paths = find_path(e)
    candidates = []
    for idx2, e2 in enumerate(paths):
        temp = 0
        for idx3, e3 in enumerate(paths):
            if idx2 == idx3:
                continue
            temp = max(dist[e2][e3], temp)
        candidates.append((temp, e2))
    ans.append(min(candidates, key=lambda x: x[0])[1])

ans.sort()

for a in ans:
    print(a)
