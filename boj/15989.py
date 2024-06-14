# 15989 1,2,3 더하기 4
# https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline


def solve(n):
    if (n < 4):
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] - dp[i - 3]
        if (i % 3 == 0):
            dp[i] += 1
    return dp[n]


T = int(input())
for i in range(T):
    n = int(input())
    print(solve(n))
