import sys
input = sys.stdin.readline

time = []
n = int(input())

for _ in range(n):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort(key = lambda x: (x[1], x[0]))

ans = 0
last_time = 0

for s, e in time:
    if s >= last_time:
        ans += 1
        last_time = e
    
print(ans)