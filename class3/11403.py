import sys
input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
    line = list(map(int, input().split()))
    info.append(line)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if info[i][k] == 1 and info[k][j] == 1:
                info[i][j] = 1

for line in info:
    for e in line:
        print(e, end=' ')
    print()
