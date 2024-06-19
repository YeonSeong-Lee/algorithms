# https://www.acmicpc.net/problem/13412

import sys
import math
input = sys.stdin.readline

t = int(input())

# gcd함수를 직접 구현하면 이런식으로! (시간 복잡도 고려함.)
# def gcd(a, b):
#   while b > 0:
#     a, b = b, a % b
#   return a


def count_disjoint_pair(n):
  cnt = 1
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0 and math.gcd(i,  n // i) == 1:
      cnt += 1
  return cnt


for _ in range(t):
  n = int(input())
  print(count_disjoint_pair(n))