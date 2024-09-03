import sys
sys.setrecursionlimit(10*10)
input = sys.stdin.readline

n, m = map(int, input().split())
root = list(range(n+1))
rank = [0 for _ in range(n+1)]


def find(a):
    if root[a] == a:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    if rank[root_a] < rank[root_b]:
        root_a, root_b = root_b, root_a
    root[root_b] = root_a
    if rank[root_a] == rank[root_b]:
        rank[root_a] += 1


def check(a, b):
    root_a = find(a)
    root_b = find(b)
    return root_a == root_b


for _ in range(m):
    w, a, b = map(int, input().split())
    if w == 0:
        union(a, b)
    else:
        if check(a, b):
            print("YES")
        else:
            print("NO")
