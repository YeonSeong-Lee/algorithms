import math
import sys
input = sys.stdin.readline

n = int(input())
nums = [-1] + list(map(int, input().split()))
m = int(input())

tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [(sys.maxsize, -1)] * tree_size


def init(node, start, end):
    if start == end:
        tree[node] = (nums[start], start)
    else:
        init(node * 2, start, (start+end) // 2)
        init(node * 2 + 1, (start + end) // 2 + 1, end)
        left = tree[node * 2]
        right = tree[node * 2 + 1]
        if left[0] <= right[0]:
            tree[node] = left
        else:
            tree[node] = right


def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        nums[start] = val
        tree[node] = (val, start)
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)
    left = tree[node * 2]
    right = tree[node * 2 + 1]
    if left <= right:
        tree[node] = left
    else:
        tree[node] = right


def query(node, start, end, left, right):
    if left > end or right < start:
        return (sys.maxsize, -1)
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_node = query(node * 2, start, mid, left, right)
    right_node = query(node * 2 + 1, mid + 1, end, left, right)
    if left_node[0] <= right_node[0]:
        return left_node
    else:
        return right_node


init(1, 1, n)

for _ in range(m):
    what, i, j = map(int, input().split())
    if what == 1:
        update(1, 1, n, i, j)
    else:
        print(query(1, 1, n, i, j)[1])
