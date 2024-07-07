import sys
input = sys.stdin.readline

def get_area_in_triangle(a, b, c):
  x1, y1 = a
  x2, y2 = b
  x3, y3 = c
  return (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)

n = int(input())
vertices = []
total = 0

for _ in range(n):
  x, y = map(int, input().split())
  vertices.append((x,y))

a = vertices[0]
for i in range(1, n-1):
  b = vertices[i]
  c = vertices[i+1]
  total += get_area_in_triangle(a, b, c)

print(round(abs(total / 2), 1))