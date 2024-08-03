import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = [0, 0, 0]
start = max(nums)
end = sum(nums)

while start <= end:
    mid = (start + end) // 2


# LEARN
# parametric search, 최적화문제를 결정문제로 전환 (종만북 찾아보기)
