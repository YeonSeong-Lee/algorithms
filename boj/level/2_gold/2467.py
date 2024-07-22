import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = sys.maxsize
start = 0
end = n - 1
a = b = 0
nums.sort()

while start < end:
    temp = abs(nums[end] + nums[start])
    if temp < ans:
        a = nums[start]
        b = nums[end]
        ans = temp
    if nums[start] + nums[end] < 0:
        start += 1
    else:
        end -= 1
print(a, b)
