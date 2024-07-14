import sys

input = sys.stdin.readline

n = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]
MOD = 1_000_000_000
ALL_VISITED = (1 << 10) - 1

for i in range(1, 10):
    dp[1][i][1 << i] = 1


for i in range(2, n + 1):
    for j in range(10):
        for visited in range(1 << 10):
            bit = visited | (1 << j)
            if j < 9:
                dp[i][j][bit] += dp[i - 1][j + 1][visited]
                dp[i][j][bit] %= MOD
            if j > 0:
                dp[i][j][bit] += dp[i - 1][j - 1][visited]
                dp[i][j][bit] %= MOD

ans = 0
for k in range(10):
    ans += dp[n][k][ALL_VISITED]
    ans %= MOD
print(ans)
