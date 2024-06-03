import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    t = int(input().strip())
    if t == 0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
    if t > 0:
        heapq.heappush(heap, t)
    