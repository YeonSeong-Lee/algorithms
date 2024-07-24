import sys
import math

input = sys.stdin.readline


def solve():
    n, m, k = map(int, input().split())
    nums = [int(input()) for _ in range(n)]
    tree_size = 1 << (math.ceil(math.log2(n)) + 1)
    tree = [1] * tree_size
    MOD = 1_000_000_007

    def init(node, start, end):
        if start == end:
            tree[node] = nums[start]
        else:
            init(node * 2, start, (start + end) // 2)
            init(node * 2 + 1, (start + end) // 2 + 1, end)
            tree[node] = (tree[2 * node] * tree[2 * node + 1]) % MOD

    def update(node, start, end, index, val):
        if index < start or index > end:
            return
        if start == end:
            nums[index] = val
            tree[node] = val
            return
        mid = (start + end) // 2
        update(node * 2, start, mid, index, val)
        update(node * 2 + 1, mid + 1, end, index, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

    def query(node, start, end, left, right):
        if left > end or right < start:
            return 1
        if left <= start and end <= right:
            return tree[node]
        mid = (start + end) // 2
        l_node = query(node * 2, start, mid, left, right)
        if l_node == 0:
            return 0
        r_node = query(node * 2 + 1, mid + 1, end, left, right)
        if r_node == 0:
            return 0
        return (l_node * r_node) % MOD

    init(1, 0, n - 1)
    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 0, n - 1, b - 1, c)
        else:
            print(query(1, 0, n - 1, b - 1, c - 1))


solve()
