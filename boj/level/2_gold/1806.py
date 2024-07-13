import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
current_sum = 0
min_length = n + 1

while True:
    if current_sum >= s:
        min_length = min(min_length, end - start)
        current_sum -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += nums[end]
        end += 1

print(min_length if min_length != n + 1 else 0)