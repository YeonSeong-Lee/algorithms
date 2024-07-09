def solve(x, y):
    if x < y or (x - y) % 2 != 0 or bin(x - y).count('1') * 2 > bin(x).count('1'):
        return 0
    else:
        return 2 ** bin(x).count('1')

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(solve(x, y))