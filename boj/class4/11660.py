import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []


lines.append([0 for _ in range(n+1)])
for _ in range(n):
  line = list(map(int, input().split()))
  line.insert(0, 0)
  for i in range(1, n+1):
    line[i] += line[i-1]
  lines.append(line)

for i in range(1, n+1):
  for j in range(n+1):
    lines[i][j] += lines[i-1][j]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  ma = lines[x2][y2]
  sub = lines[x1-1][y2] + lines[x2][y1-1]
  com = lines[x1-1][y1-1]
  print(ma - sub + com)
