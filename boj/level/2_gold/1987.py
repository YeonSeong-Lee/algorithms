import sys
input = sys.stdin.readline

r, c = map(int, input().split())
visited = [0] * 26
graph = []
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(r):
    line = input().strip()
    graph.append(line)


def dfs(i, j):
    global ans
    ans = max(ans, sum(visited))
    if ans == r * c:
        print(ans)
        exit()
    for dy, dx in dir:
        ny, nx = i + dy, j + dx
        if ny >= r or ny < 0 or nx >= c or nx < 0:
            continue
        if visited[ord(graph[ny][nx]) - ord('A')] == 1:
            continue
        visited[ord(graph[ny][nx]) - ord('A')] = 1
        dfs(ny, nx)
        visited[ord(graph[ny][nx]) - ord('A')] = 0


ans = 0
visited[ord(graph[0][0]) - ord('A')] = 1
dfs(0, 0)

print(ans)
