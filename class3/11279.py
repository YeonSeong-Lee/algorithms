import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    n = -int(input().strip())
    if n == 0 and len(heap) == 0:
        print(0)
    if n == 0 and len(heap) > 0:
        print(-heapq.heappop(heap))
    else:
       heapq.heappush(heap, n)
       