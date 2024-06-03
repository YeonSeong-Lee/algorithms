import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    wear = {}
    n = int(input())
    for j in range(n):
        name, kind = input().split()
        wear[kind] = wear.get(kind, 1) + 1
    ans = 1
    for k, v in wear.items():
        ans *= v
    print(ans - 1)
