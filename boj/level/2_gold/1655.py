import heapq
import sys
input = sys.stdin.readline

n = int(input())

left = []
right = []
heapq.heapify(left)
heapq.heapify(right)

for _ in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)
    print(-left[0])

# LEARN
# 우선순위큐, 정렬된 값중 특정 값만 빠르게 필요할 때 쓸 수 있는 테크닉