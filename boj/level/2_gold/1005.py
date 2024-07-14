from collections import defaultdict, deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    graph = defaultdict(list)
    n, k = map(int, input().split())
    in_degree = [0 for _ in range(n + 1)]
    delay = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1
    w = int(input())

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = delay[i]
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[cur] + delay[i])
            if in_degree[i] == 0:
                q.append(i)

    print(dp[w])
