import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = {}
no_hear_and_watch = []
for _ in range(n):
    name = input().strip()
    no_hear[name] = True


for _ in range(m):
    name = input().strip()
    if name in no_hear:
        no_hear_and_watch.append(name)

no_hear_and_watch.sort()

print(len(no_hear_and_watch))
for e in no_hear_and_watch:
    print(e)
