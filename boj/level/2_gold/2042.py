import sys
import math
input = sys.stdin.readline

def init(nums, tree, node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        init(nums, tree, node * 2, start, (start + end) // 2)
        init(nums, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node * 2, start, (start+end) // 2, left, right)
    rsum = query(tree, node * 2 + 1, (start+end)//2 + 1, end, left, right)
    return lsum + rsum

def update(nums, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        nums[index] = val
        tree[node] = val
        return
    update(nums, tree, node * 2, start, (start+end)//2, index, val)
    update(nums, tree, node * 2 + 1, (start+end)//2 + 1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2 + 1]

n, m, k = map(int, input().split())
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
nums = [int(input()) for _ in range(n)]

init(nums, tree, 1, 0, n-1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(nums, tree, 1, 0, n-1, b-1, c)
    else:
        print(query(tree, 1, 0, n-1, b-1, c-1))