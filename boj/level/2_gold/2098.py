import sys
input = sys.stdin.readline

n = int(input())
weight = []

for _ in range(n):
    line = list(map(int, input().split()))
    weight.append(line)

