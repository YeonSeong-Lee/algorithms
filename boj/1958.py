import sys
input = sys.stdin.readline

a = ' ' + input().strip()
b = ' ' + input().strip()
c = ' ' + input().strip()

n, m, o = len(a), len(b), len(c)
dp = [[[0] * o for _ in range(m)] for _ in range(n)]


for i in range(1, n):
    for j in range(1, m):
        for k in range(1, o):
            if a[i] == b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])
