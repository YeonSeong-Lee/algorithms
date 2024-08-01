import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())


def bellman_ford(n, graph):
    upper = [sys.maxsize for _ in range(n+1)]
    for _ in range(1, n+1):
        update = False
        for here in range(1, n+1):
            for there, cost in graph[here]:
                if upper[there] > upper[here] + cost:
                    upper[there] = upper[here] + cost
                    update = True
        if update == False:
            break
    if update:
        return "YES"
    else:
        return "NO"


def solve(n, m, w):
    graph = defaultdict(list)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    print(bellman_ford(n, graph))


for _ in range(t):
    n, m, w = map(int, input().split())
    solve(n, m, w)
