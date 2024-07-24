import sys
import math

input = sys.stdin.readline


def init(nums, tree, node, start, end):
    if start == end:
        tree[node] = (nums[start], nums[start])
    else:
        init(nums, tree, node * 2, start, (start + end) // 2)
        init(nums, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        l_node = tree[node * 2]
        r_node = tree[node * 2 + 1]
        tree[node] = (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]))


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return (sys.maxsize, 0)
    if left <= start and end <= right:
        return tree[node]
    l_node = query(tree, node * 2, start, (start + end) // 2, left, right)
    r_node = query(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]))


def update(nums, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        nums[index] = val
        tree[node] = val
        return
    update(nums, tree, node * 2, start, (start + end) // 2, index, val)
    update(nums, tree, node * 2 + 1, (start + end) // 2 + 1, end, index, val)
    l_node = tree[node * 2]
    r_node = tree[node * 2 + 1]
    tree[node] = (min(l_node[0], r_node[0]), max(l_node[1], l_node[1]))


n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]
tree = [(sys.maxsize, 0)] * (1 << (math.ceil(math.log2(n)) + 1))
init(nums, tree, 1, 0, n - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(*query(tree, 1, 0, n - 1, a - 1, b - 1))
