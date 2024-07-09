import sys
input = sys.stdin.readline

def convert_to_origin(lst, lst2):
  min_1, min_2 = min(lst), min(lst2)
  if min_1 > 0:
    min_1 = 0
  if min_2 > 0:
    min_2 = 0
  return list(map(lambda x, y: (x - min_1, y - min_2), lst, lst2))

_ = int(input())
maze = input().strip()
dir = [0, -1]
cur_x = 0
cur_y = 0
track_x = [cur_x]
track_y = [cur_y]

for s in maze:
  if s == 'F':
    cur_x += dir[0]
    cur_y += dir[1]
    track_x.append(cur_x)
    track_y.append(cur_y)
  if s == 'L':
    temp = dir[0]
    dir[0] = -dir[1]
    dir[1] = temp
  if s == 'R':
    temp = dir[0]
    dir[0] = dir[1]
    dir[1] = -temp


track = convert_to_origin(track_x, track_y)
max_x = max(list(map(lambda x: x[0], track)))
max_y = max(list(map(lambda x: x[1], track)))

visited = [[0] * (max_x+1) for _ in range(max_y+1)]

for tx, ty in track:
  visited[ty][tx] = 1

for i in range(max_y, -1, -1):
  for j in range(0, max_x + 1):
    if visited[i][j] == 1:
      print('.', end='')
    else:
      print('#', end='')
  print()


