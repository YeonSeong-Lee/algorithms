import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n + 1)
parent = [0] * (n + 1)


def dfs(i, d):
    depth[i] = d
    for e in graph[i]:
        if depth[e] > 0 or e == 1:
            continue
        parent[e] = i
        dfs(e, d + 1)


dfs(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[b] != depth[a]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(b)

# LEARN
# 최소공통조상 찾기 기본적인 알고리즘
