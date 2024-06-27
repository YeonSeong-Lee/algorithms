import sys
input = sys.stdin.readline

n = int(input())
p = []

p = list(map(int, input().split()))
p.sort()

cur = 0
total = 0
for e in p:
    cur += e
    total += cur

print(total)
