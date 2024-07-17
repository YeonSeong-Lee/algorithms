import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))

for _ in range(k):
    bags.append(int(input()))

jewels.sort()
bags.sort()

total_value = 0
available_jewels = []

j = 0
for bag in bags:
    while j < n and jewels[j][0] <= bag:
        heapq.heappush(available_jewels, -jewels[j][1])
        j += 1
    if available_jewels:
        total_value -= heapq.heappop(available_jewels)

print(total_value)
