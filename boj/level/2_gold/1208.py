import sys
from itertools import combinations
import bisect

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

half = n // 2
left_part = nums[:half]
right_part = nums[half:]


def get_subsequence_sums(arr):
    subseq_sums = [0]
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            subseq_sums.append(sum(comb))
    return subseq_sums


left_sums = get_subsequence_sums(left_part)
right_sums = get_subsequence_sums(right_part)

right_sums.sort()

cnt = 0
for left_sum in left_sums:
    target = s - left_sum
    lower_bound = bisect.bisect_left(right_sums, target)
    upper_bound = bisect.bisect_right(right_sums, target)
    cnt += upper_bound - lower_bound

if s == 0:
    cnt -= 1
print(cnt)

# LEARN
# meet in the middle, 반 나누기.
