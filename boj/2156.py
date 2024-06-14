# 2156 포도주 시식
import sys
input = sys.stdin.readline

N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0] * N

dp[0] = wines[0]
if (N > 1):
    dp[1] = wines[0] + wines[1]
if (N > 2):
    dp[2] = max(wines[2] + wines[1], wines[2] + wines[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i -3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i])

print(dp[N - 1])

