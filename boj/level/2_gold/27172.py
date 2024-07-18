import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
score = [0] * n
max_num = max(nums)
nums_index = {num: idx for idx, num in enumerate(nums)}

for i in range(n):
    cur = nums[i]
    for j in range(cur * 2, max_num + 1, cur):
        if j in nums_index:
            score[i] += 1
            idx = nums_index[j]
            score[idx] -= 1

print(*score)

# 배운 점
# 정렬이 필요한데 원래 순서를 기억해야할 필요가 있을 때는 dict로 인덱스를 기억하고 있기!
