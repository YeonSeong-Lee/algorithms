import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
c = list(map(int, input().split()))

males = []
females = []
root = [0] * (n + 1)
rank = [0] * (n + 1)
for i in range(1, n + 1):
    root[i] = i

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
    if rank[x] == rank[y]:
        rank[x] += 1

def find_all_set():
    candidates = []
    for e in range(1, n + 1):
        temp = root[e]
        if temp not in candidates:
            candidates.append(temp)
    return candidates

def find_couple(root):
    elements = []
    cnt = 0
    for i in range(1, n + 1):
        if find(i) == root:
            elements.append(i)
    comb = list(combinations(elements, 2))
    
    for e in comb:
        if e[0] in males and e[1] in females:
            cnt += 1
        if e[0] in females and e[1] in males:
            cnt += 1
    return cnt
    
    

for i, e in enumerate(c):
    if e % 2 == 0:
        females.append(i + 1)
    else:
        males.append(i + 1)


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    candidates = find_all_set()
    ans = 0
    for candidate in candidates:
        ans += find_couple(candidate)
    print(ans)
