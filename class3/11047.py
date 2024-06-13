import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
ans = 0
for _ in range(n):
    coins.append(int(input().strip()))

for i in range(len(coins) - 1, -1, -1):
    if k == 0:
        break
    temp = k // coins[i]
    if temp > 0:
        ans += temp
        k -= temp * coins[i]

print(ans)