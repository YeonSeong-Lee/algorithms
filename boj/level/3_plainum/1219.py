from collections import defaultdict
import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())
traffic = defaultdict(list)
reachable = [[sys.maxsize] * n for _ in range(n)]
for _ in range(m):
    s, e, c = map(int, input().split())
    traffic[s].append((e, c))
    reachable[s][e] = c
incomes = list(map(int, input().split()))
money = [sys.maxsize for _ in range(n)]
money[start] = -incomes[start]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                reachable[i][j] = 0
            else:
                reachable[i][j] = min(
                    reachable[i][j], reachable[i][k] + reachable[k][j])


if reachable[start][end] == sys.maxsize:
    print("gg")
    exit()

for _ in range(n-1):
    for here in range(n):
        for there, cost in traffic[here]:
            if money[here] == sys.maxsize:
                continue
            if money[there] > money[here] + cost - incomes[there]:
                money[there] = money[here] + cost - incomes[there]

for here in range(n):
    for there, cost in traffic[here]:
        if money[here] == sys.maxsize:
            continue
        if money[there] > money[here] + cost - incomes[there]:
            if reachable[start][here] != sys.maxsize and reachable[here][end] != sys.maxsize:
                print("Gee")
                exit()


print(-money[end])
