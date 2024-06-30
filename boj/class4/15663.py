import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
store = []
visited = [False] * n
data = []
def dfs():
  last = 0
  if len(store) == m:
      print(*store)
      return
  for i, e in enumerate(nums):
    if visited[i] == True or e == last:
      continue
    visited[i] = True
    store.append(e)
    last = e
    dfs()
    store.pop()
    visited[i] = False

dfs()
