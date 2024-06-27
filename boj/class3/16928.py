import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = []
snack = []
dp = [0 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    ladder.append((x, y))

for _ in range(m):
    x, y = map(int, input().split())
    snack.append((x, y))

