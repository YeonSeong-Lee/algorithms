import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = [0, 0, 0]
start = max(nums)
end = sum(nums)

while start <= end:
    mid = (start + end) // 2
