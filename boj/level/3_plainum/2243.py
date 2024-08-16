import sys
input = sys.stdin.readline

n = int(input())
MAX_TASTE = 1000000
tree = [0] * 4 * MAX_TASTE


def query(node, start, end, k):
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[node * 2] >= k:
        return query(node * 2, start, mid, k)
    else:
        return query(node * 2 + 1, mid + 1, end, k - tree[node * 2])


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        tree[node] += diff
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, index, diff)
    update(node * 2 + 1, mid + 1, end, index, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    

for _ in range(n):
    what, *cmd = map(int, input().split())
    if what == 1:
        taste = query(1, 1, MAX_TASTE , cmd[0])
        print(taste)
        update(1, 1, MAX_TASTE, taste, -1)
    else:
        update(1, 1, MAX_TASTE, cmd[0], cmd[1])
