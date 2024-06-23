import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def min_command(a, b):
    visited = [0 for _ in range(10001)]
    dir = ['D', 'S', 'L', 'R']
    q = deque()
    q.append((a, ''))
    visited[a] = 1
    while q:
        cur_num, cur_command = q.popleft()
        if cur_num == b:
            print(cur_command)
            break
        for v in dir:
            temp = 0
            if v == 'D':
                temp = (2 * cur_num) % 10000
            if v == 'S':
                temp = cur_num - 1
                if cur_num == 0:
                    temp = 9999
            if v == 'L':
                temp = (cur_num % 1000) * 10 + cur_num // 1000
            if v == 'R':
                temp = (cur_num % 10) * 1000 + (cur_num - cur_num % 10) // 10
            if visited[temp] == 1:
                continue
            visited[temp] = 1
            q.append((temp, cur_command + v))


for _ in range(t):
    a, b = map(int, input().split())
    min_command(a, b)
