import sys
input = sys.stdin.readline

n = int(input())

def golomb(n):
  if n == 1:
    return 1
  return 1 + golomb(n - golomb(golomb(n-1)))

print(golomb(n))