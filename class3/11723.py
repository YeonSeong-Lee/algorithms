import sys
input = sys.stdin.readline

n = int(input())
data = 0
for _ in range(n):
    line = input().split()
    if len(line) > 1:
        num = int(line[1]) - 1
    oper = line[0]
    if oper == 'add':
        data |= 1 << num
    if oper == 'remove':
        data &= ~(1 << num)
    if oper == 'check':
        if data & 1 << num:
            print(1)
        else:
            print(0)
    if oper == 'toggle':
        data ^= 1 << num
    if oper == 'all':
        data = (1 << 20) - 1
    if oper == 'empty':
        data = 0
