import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
score = [0] * n

for i in range(n):
    for j in range(i, n):
        player = nums[i]
        opponent = nums[j]
        if opponent % player == 0:
            score[i] += 1
            score[j] -= 1
        elif player % opponent == 0:
            score[i] -= 1
            score[j] += 1

print(*score)
