from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = n * n


def get_rank(mid):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    return cnt


ans = 0
while start <= end:
    mid = (start + end) // 2
    if get_rank(mid) < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)
