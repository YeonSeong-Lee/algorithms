import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
c = list(map(int, input().split()))

for i, e in enumerate(c):
    if e % 2 == 0:
        c[i] = 0
    else:
        c[i] = 1

root = [0] * (n + 1)
rank = [0] * (n + 1)
candidates = [0] * (n)
for i in range(1, n + 1):
    root[i] = i
    candidates[i-1] = i

def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        x, y = y, x
    root[y] = x
    candidates.remove(y)
    if rank[x] == rank[y]:
        rank[x] += 1

def find_couple(root):
    elements = []
    cnt = 0
    for i in range(1, n + 1):
        if find(i) == root:
            elements.append(i)
    comb = list(combinations(elements, 2))
    
    for a, b in comb:
        if c[a-1] != c[b-1]:
            cnt += 1
    return cnt



for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    ans = 0
    for candidate in candidates:
        ans += find_couple(candidate)
    print(ans)
