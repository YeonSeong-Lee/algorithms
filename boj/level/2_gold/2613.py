import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = max(nums)
end = sum(nums)
ans = []


def count_group(size):
    group_cnt = 0
    group = []
    i = 0
    while i < n:
        sub_sum = 0
        sub_cnt = 0
        while i < n and sub_sum + nums[i] <= mid:
            sub_sum += nums[i]
            sub_cnt += 1
            i += 1
            if group_cnt + n - i + 1 == m:
                break
        group_cnt += 1
        group.append(sub_cnt)

    return group_cnt, group


while start <= end:
    mid = (start + end) // 2
    temp_m, ans = count_group(mid)
    if temp_m <= m:
        ans_mid = mid
        ans_ans = ans
        end = mid - 1
    else:
        start = mid + 1

print(ans_mid)
print(*ans_ans)

# LEARN
# parametric search, 최적화문제를 결정문제로 전환 (종만북 찾아보기)
# 이분탐색시 답 저장해두기.
