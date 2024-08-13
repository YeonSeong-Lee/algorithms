import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

dp = [[0] * (n) for _ in range(n)]
for i in range(n):
    dp[i][i] = 1


for size in range(2, n + 1):
    for i in range(n - size + 1):
        j = i + size - 1
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]

print(dp[0][n-1])
# LEARN
# dp, 점화식이 양쪽으로 돌 수도 있음. (팰린드롬),  MOD나누기할 때 빼기가 있을 수 도 있음에 주의
