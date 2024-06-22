import sys
input = sys.stdin.readline

def is_empty_horizon():
  if xi[0] > w / 2:
    return True
  if xi[-1] < 75 - w / 2:
    return True
  for i in range(1, len(xi)):
    if xi[i] > 75 and xi[i-1] + w / 2 > xi[i] - w / 2:
      return False
    gap = xi[i] - xi[i-1]
    if gap > w:
      return True
  return False


def is_empty_vertical():
  if yi[0] > w / 2:
    return True
  if yi[-1] < 100 - w / 2:
    return True
  for i in range(1, len(yi)):
    if yi[i] > 100 and yi[i-1] + w / 2 > yi[i] - w / 2:
      return False
    gap = yi[i] - yi[i-1]
    if gap > w:
      return True
  return False

while True:
  nx, ny, w = map(float, (input().split()))
  if nx == 0 and ny == 0 and w == 0.0:
    break
  xi = list(map(float, input().split()))
  yi = list(map(float, input().split()))
  xi.sort()
  yi.sort()

  if is_empty_horizon() or is_empty_vertical():
    print("NO")
  else:
    print("YES")