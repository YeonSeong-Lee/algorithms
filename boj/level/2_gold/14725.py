from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
s = deque()
visited = set()
start_point = []
for _ in range(n):
    line = input().split()[1:]
    key = 0
    if (0, line[0], 0) not in start_point:
        start_point.append((0, line[0], 0))
    for i, e in enumerate(line):
        if i == len(line) - 1:
            break
        key = (i, line[i], key)
        graph[key].append((i+1, line[i+1], key))
        graph[key].sort(reverse=True)

start_point.sort(reverse=True)

for e in start_point:
    s.append(e)
    visited.add(e)

while s:
    cur_i, cur_e, p = s.pop()
    print("--" * cur_i, end='')
    print(cur_e)
    for ni, ne, np in graph[(cur_i, cur_e, p)]:
        if (ni, ne, np) not in visited:
            visited.add((ni, ne, np))
            s.append((ni, ne, np))

# LEARN
# stack으로 dfs 돌 때 주의, 트라이 자료구조의 기초적인 형태