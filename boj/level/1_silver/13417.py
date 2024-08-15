import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def solve():
    _ = int(input())
    alphabets = list(input().split())
    res = deque([alphabets[0]])
    for e in alphabets[1:]:
        if res[0] < e:
            res.append(e)
        else:
            res.appendleft(e)
    print(''.join(res))


for _ in range(t):
    solve()
