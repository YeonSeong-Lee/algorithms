import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())
root = list(range(n + 1))
rank = [0 for _ in range(n + 1)]
graph = []


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return False
    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True


ans = 0
for _ in range(m):
    u, v = map(int, input().split())
    # 이미 같은 집합이면
    if union(u, v) == False:
        ans += 1


def count_unique(arr):
    return len(set(arr))


for i in range(1, n+1):
    find(i)

print(count_unique(root[1:]) - 1 + ans)
