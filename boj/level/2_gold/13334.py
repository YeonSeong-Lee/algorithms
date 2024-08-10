import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    house, office = map(int, input().split())
    if house > office:
        house, office = office, house
    data.append((house, office))
data.sort(key=lambda x: x[1])



d = int(input())

ans = 0
heap = []

for h, o in data:
    if o - h <= d:
        heapq.heappush(heap, h)
    while heap and heap[0] < o - d:
        heapq.heappop(heap)
    ans = max(ans, len(heap))

print(ans)

# LEARN:
# sweeping 알고리즘, 문제가 간단해지는 정렬기준 찾기, while문으로 조건에 부합하지 않는 것들 지우기, 
# 집합관점에서 풀 수도 있음.