import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def dfs(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n+1):
        ans.append(nums[i-1])
        dfs(i)
        ans.pop()

dfs(1)