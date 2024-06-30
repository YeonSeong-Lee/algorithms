import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
store = []
def dfs():
  if len(store) == m:
      print(*store)
      return
  last = 0
  for i, e in enumerate(nums):
    if last == e:
      continue
    if len(store) > 0 and e < store[-1]:
      continue
    store.append(e)
    last = e
    dfs()
    store.pop()

dfs()
