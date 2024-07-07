import sys
input = sys.stdin.readline

def get_area_in_triangle(a, b, c):
  x1, y1 = a
  x2, y2 = b
  x3, y3 = c
  return abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) / 2

n = int(input())
veterx = []
total = 0

for _ in range(n):
  x, y = map(int, input().split())
  veterx.append((x,y))

a = veterx[0]
for i in range(1, n-1):
  b = veterx[i]
  c = veterx[i+1]
  total += get_area_in_triangle(a, b, c)

print(round(total, 1))