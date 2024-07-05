import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

def bfs():
    q = deque([(a, 1)])

    while q:
        cur, op = q.popleft()
        if cur == b:
            print(op)
            return
        for _ in range(2):
            if _  == 0 and 2 * cur <= b:
                q.append((2 * cur, op + 1))
            elif 10 * cur + 1 <= b:
                q.append((10 * cur + 1, op + 1))
    print(-1)

bfs()