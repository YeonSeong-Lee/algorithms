from collections import defaultdict, deque
import sys

input = sys.stdin.readline
n = int(input())
graph = defaultdict(list)
time = [0 for _ in range(n + 1)]
in_dgree = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    nums = list(map(int, input().split()))
    time[_ + 1] = nums[0]
    prev = nums[1:-1]
    for e in prev:
        graph[e].append(_ + 1)
        in_dgree[_ + 1] += 1
q = deque()

for i in range(1, n + 1):
    if in_dgree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    cur = q.popleft()
    for e in graph[cur]:
        in_dgree[e] -= 1
        dp[e] = max(dp[e], dp[cur] + time[e])
        if in_dgree[e] == 0:
            q.append(e)

for i in range(1, n + 1):
    print(dp[i])
