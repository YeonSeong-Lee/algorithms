from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
dp = [[0, 1] for _ in range(n+1)]


def dfs(i):
    visited.add(i)
    for ne in graph[i]:
        if ne in visited:
            continue
        dfs(ne)
        dp[i][0] += dp[ne][1]
        dp[i][1] += min(dp[ne][1], dp[ne][0])
    
dfs(1)
print(min(dp[1]))