import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
r_ans = []

def dfs(start):
    if sum(ans) >= s:
        r_ans.append(len(ans))
        return
    for i in range(start, len(nums)):
        ans.append(nums[i])
        dfs(i+1)
        ans.pop()

dfs(0)
print(min(r_ans) if len(r_ans) > 0 else 0)