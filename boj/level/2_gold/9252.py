import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a = ' ' + input().strip()
b = ' ' + input().strip()
m, n = len(b), len(a)
dp = [[0] * n for _ in range(m)]
back = [[0] * n for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + 1
            back[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i-1][j] > dp[i][j-1]:
                back[i][j] = 2
            else:
                back[i][j] = 3


print(dp[-1][-1])


def get_path(i, j):
    if i == 0 or j == 0:
        return ''
    temp = back[i][j]
    if temp == 1:
        return get_path(i-1, j-1) + a[j]
    elif temp == 2:
        return get_path(i-1, j)
    else:
        return get_path(i, j-1)


print(get_path(m-1, n-1))
