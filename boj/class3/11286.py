import heapq
import sys
input = sys.stdin.readline

t = int(input())
heap = []
for _ in range(t):
    n = int(input().strip())
    if n == 0 and len(heap) == 0:
        print(0)
        continue
    if n == 0 and len(heap) > 0:
        print(heapq.heappop(heap)[1])
    else:
       heapq.heappush(heap, (abs(n), n))
    