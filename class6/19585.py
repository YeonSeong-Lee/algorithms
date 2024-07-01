import sys
input = sys.stdin.readline

c, n = map(int, input().split())
colors = {}
names = {}

def is_legend(word):
    now = colors
    for i in range(len(word)):
        if now.get(0) and word[i:] in names:
            print("Yes")
            return 1
        if not now.get(word[i]):
            print("No")
            return
        now = now[word[i]]


for _ in range(c):
    now = colors
    for i in input().strip():
        if not now.get(i):
            now[i] = {}
        now = now[i]
    now[0] = 1

names = {input().strip() for i in range(n)}

q = int(input())

for _ in range(q):
    is_legend(input().strip())
