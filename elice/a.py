import heapq
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return min(root_x, root_y)

def solve(n, colors):
    red_edge = 0
    for color in colors:
        min_increse = sys.maxsize
        max_increse = 0
        s_u, s_v = -1, -1
        # 빨간색일 떄
        if color == 0:
            for u in range(2, n + 1):
                for v in range(u + 1, n + 1):
                    if find(u) != find(v):
                        temp_increase = sizes[find(u)] * sizes[find(v)]
                        if temp_increase < min_increse:
                            min_increse = temp_increase
                            s_u, s_v = u, v
            red_edge += min_increse
            root = union(s_u, s_v)
            sizes[root] += temp_increase
        # 파란색 간선일 때
        else:
            for u in range(1, n + 1):
                for v in range(u + 1, n + 1):
                    if find(u) != find(v):
                        temp_increase = sizes[find(u)] * sizes[find(v)]
                        if temp_increase > max_increse:
                            max_increse = temp_increase
                            s_u, s_v = u, v
            root = union(s_u, s_v)
            sizes[root] += temp_increase
    return red_edge

n = int(input())
colors = list(map(int, input().split()))
parent = [i for i in range(n+1)]
sizes = [1 for _ in range(n+1)]
print('sizes', sizes)
ans = solve(n, colors)
print(ans)