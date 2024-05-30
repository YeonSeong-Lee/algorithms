import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
pre_sum = [0] * (n+1)

for i in range(1, n+1):

    pre_sum[i] = pre_sum[i-1] + data[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(pre_sum[j] - pre_sum[i-1])
     