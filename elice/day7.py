import sys

input = sys.stdin.readline

n, k = map(int, input().split())
CASE = 1 << 10
length = len(str(n))
dp = [[sys.maxsize] * CASE for _ in range(length + 2)]

for i in range(1, 10):
    dp[1][1 << i] = i


for i in range(2, length + 2):
    for j in range(10):
        for bit in range(CASE):
            temp = dp[i - 1][bit]
            if temp == sys.maxsize:
                continue
            temp = 10 * temp + j
            if i == length and temp > n:
                dp[i][bit | (1 << j)] = min(temp, dp[i][bit | (1 << j)])
            else:
                dp[i][bit | (1 << j)] = min(temp, dp[i][bit | (1 << j)])

ans = sys.maxsize
if n < int(length * '9'):
    for i, e in enumerate(dp[length]):
        if e == sys.maxsize:
            continue
        if bin(i).count("1") == k and e > n:
            ans = min(ans, e)
else:
    for i, e in enumerate(dp[length+1]):
        if e == sys.maxsize:
            continue
        if bin(i).count("1") == k and e > n:
            ans = min(ans, e)

print(ans if ans < sys.maxsize else -1)
