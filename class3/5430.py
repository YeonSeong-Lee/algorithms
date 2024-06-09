import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    oper = input().strip()
    n = int(input().strip())
    error_flag = False
    dir_flag = 1
    data = deque(input()[1:-2].split(','))
    if n == 0:
        data = []
    for s in oper:
        if s == 'R':
            dir_flag *= -1
        if s == 'D':
            if len(data) > 0:
                if dir_flag == 1:
                    data.popleft()
                else:
                    data.pop()
            else:
                error_flag = True
                break

    if error_flag:
        print("error")
    else:
        if dir_flag == -1:
            data.reverse()
        print('[' + ','.join(data) + ']')
