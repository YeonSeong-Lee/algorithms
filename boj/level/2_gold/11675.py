import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
upper = [sys.maxsize for _ in range(n+1)]


def bellman_ford(start):
    upper[start] = 0
    for _ in range(1, n+1):
        updated = False
        for here in range(1, n+1):
            for there, cost in graph[here]:
                if upper[here] == sys.maxsize:
                    continue
                if upper[there] > upper[here] + cost:
                    upper[there] = upper[here] + cost
                    updated = True
        if updated == False:
            break
    if updated:
        return -1
    return upper


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

negative_cycle = bellman_ford(1)
if negative_cycle == -1:
    print(-1)
    exit()

for i in range(2, n+1):
    if upper[i] == sys.maxsize:
        print(-1)
    else:
        print(upper[i])
