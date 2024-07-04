import sys
input = sys.stdin.readline

_ = int(input())
maze = input().strip()
dir = [0, 1]
cur = [0, 0]
track = [[0, 0]]

for s in maze:
  if s == 'F':
    cur[0] += dir[0]
    cur[1] += dir[1]
    track.append(cur)
  if s == 'L':
    temp = dir[0]
    dir[0] = -dir[1]
    dir[1] = temp
  if s == 'R':
    temp = dir[0]
    dir[0] = dir[1]
    dir[1] = -temp

print(*track)