import sys
input = sys.stdin.readline

q = int(input())

for _ in range(q):
    cnt = 0
    x, y = map(int, input().split())
    for i in range(x):
        if i ^ (x - i) == y:
            cnt += 1
    print(cnt)
