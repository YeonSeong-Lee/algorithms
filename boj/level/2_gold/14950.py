import sys
import heapq
input = sys.stdin.readline


n, m, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
q = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

cnt_t = 0
ans = 0
visited = set()

heapq.heappush(q, (0, 1))

while q:
    cur_w, cur_node = heapq.heappop(q)
    if cur_node in visited:
        continue
    visited.add(cur_node)
    if cur_node != 1:
        ans += cur_w + t * cnt_t
        cnt_t += 1
    if len(visited) == n:
        break
    for nw, nn in graph[cur_node]:
        heapq.heappush(q, (nw, nn))
print(ans)
