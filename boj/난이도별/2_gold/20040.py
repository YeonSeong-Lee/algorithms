import sys
input = sys.stdin.readline
n, m = map(int, input().split())
head = [i for i in range(n)]

def get_root(x):
  if head[x] == x:
    return x
  else:
    head[x] = get_root(head[x])
    return head[x]

def union(a, b):
  x = get_root(a)
  y = get_root(b)
  if x < y:
    head[y] = x
  else:
    head[x] = y

flag = False
res = 1
for _ in range(m):
  a, b = map(int, input().split())
  if get_root(a) == get_root(b):
    flag = True
    break
  union(a, b)
  res += 1

if flag:
  print(res)
else:
  print(0)