from math import log2
import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n+1)
k_max = int(log2(n) + 1)
parent = [[0] * (k_max + 1) for _ in range(n+1)]


def dfs(i, d):
    depth[i] = d
    for e in graph[i]:
        if depth[e] > 0 or e == 1:
            continue
        parent[e][0] = i
        dfs(e, d + 1)


dfs(1, 0)
for i in range(1, k_max):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(k_max - 1, -1, -1):
        diff = depth[b] - depth[a]
        if diff >= (1 << i):
            b = parent[b][i]
    if a == b:
        print(a)
        continue
    for i in range(k_max, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    print(parent[a][0])

# LEARN
# 최소공통조상 찾기, 그래프 탐색하기위해 조상들을 저장해두고 빠르게 올라가기,
