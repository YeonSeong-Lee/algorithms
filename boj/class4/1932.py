import sys
input = sys.stdin.readline

r = int(input().strip())
lines = []
for _ in range(r):
    line = list(map(int, input().split()))
    line.insert(0, 0)
    line.append(0)
    lines.append(line)

for i in range(1, r):
    for j in range(1, i+2):
        lines[i][j] += max(lines[i-1][j-1], lines[i-1][j])

print(max(lines[r-1]))
