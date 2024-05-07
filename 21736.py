from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split());
info = []
start = ()

for i in range(N):
  r = list(input().rstrip())
  for j in range(M):
    if (r[j] == 'I'):
      start = (i, j)
  info.append(r)

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * M for _ in range(N)]
cnt = 0

q = deque([start])
visited[start[0]][start[1]] = True
while(q):
  x, y = q.popleft()
  
  for dx, dy in direction:
    nx, ny = x + dx, y + dy

    if 0 <= nx < N and 0 <= ny < M:
      if info[nx][ny] != 'X' and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
        if (info[nx][ny] == 'P'):
          cnt += 1

print(cnt if cnt > 0 else 'TT')


