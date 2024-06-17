import sys
input = sys.stdin.readline

n = int(input())
colors = []

for _ in range(n):
    r, g, b = map(int, input().split())
    colors.append([r, g, b])

for _ in range(n - 2, -1, -1):
    for i in range(3):
        temp_min = 1e9
        for j in range(3):
            if j == i:
                continue
            temp_min = min(temp_min, colors[_ + 1][j])
        colors[_][i] += temp_min

print(min(colors[0]))
