import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input().strip())
    min_heap = []
    max_heap = []
    visited = [0] * k
    for _ in range(k):
        oper, n = input().split()
        n = int(n)
        if oper == 'I':
            heapq.heappush(min_heap, (n, _))
            heapq.heappush(max_heap, (-n, _))
        if oper == 'D':
            if len(min_heap) == 0:
                continue
            if n == 1:
                idx = heapq.heappop(max_heap)[1]
                visited[idx] = 1
            else:
                idx = heapq.heappop(min_heap)[1]
                visited[idx] = 1
        while max_heap and visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
