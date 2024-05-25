import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dir = ['D', 'S', 'L', 'R']
# 유의!: 어디를 방문처리할지 생각!
def bfs(oper, fr, to):
    if fr == to:
        print(oper)
    for v in dir:
        oper = oper + v
        if v == 'D':
            temp = D(fr)
            bfs(oper, temp, to)
        elif v == 'S':
            temp = S(fr)
            bfs(oper, temp, to)
        elif v == 'L':
            temp = L(fr)
            bfs(oper, temp, to)
        elif v == 'R':
            temp = R(fr)
            bfs(oper, temp, to)

for _ in range(n):
    fr, to = map(int, input().split())
    bfs(fr, to)
