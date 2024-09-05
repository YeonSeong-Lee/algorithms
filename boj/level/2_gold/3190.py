import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
k = int(input())
apples = []
operations = [''] * (n*n)
snake = deque()

for _ in range(k):
    r, c = map(int, input().split())
    apples.append((r, c))

dir = [0, 1]

l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    operations[x] = c


def detect_collision(i, j):
    if i == 0 or i == n + 1:
        return True
    if j == 0 or j == n + 1:
        return True
    if (i, j) in snake:
        return True
    return False

cnt = 0
i, j = 1, 1
snake.append((i, j))
while True:
    cnt += 1
    dy, dx = dir
    i, j = i + dy, j + dx
    if detect_collision(i, j):
        print(cnt)
        exit()
    if (i, j) in snake:
        print(cnt)
        exit()
    snake.append((i, j))
    if (i, j) not in apples:
        snake.popleft()
    else:
        apples.remove((i, j))
    if operations[cnt] != '':
        if operations[cnt] == 'D':
            dir[1], dir[0] = -dir[0], dir[1]
        if operations[cnt] == 'L':
            dir[1], dir[0] = dir[0], -dir[1]
