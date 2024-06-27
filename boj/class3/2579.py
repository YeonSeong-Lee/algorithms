import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 301
staris = [0] * 301

for i in range(1, n+1):
    staris[i] = int(input())
dp[1] = staris[1]
dp[2] = staris[2] + staris[1]
dp[3] = max(staris[1] + staris[3], staris[2] + staris[3])

for i in range(4, n+1):
    dp[i] += staris[i]
    dp[i] += max(dp[i-3] + staris[i-1], dp[i-2])
print(dp[n])
