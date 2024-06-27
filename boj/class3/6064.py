import sys
input = sys.stdin.readline

t = int(input())

def count_cain(m, n, x, y):
    ma = max(m, n)
    ans = x
    if ma == n:
        ans = y
    while ans <= m * n:
        if (ans - x) % m == 0 and (ans - y) % n == 0:
            return ans
        ans += ma
    return -1

for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(count_cain(m, n, x, y))
