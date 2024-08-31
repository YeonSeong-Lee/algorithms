import copy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
res = []


def dfs(stack, sequence, next_num):
    if len(sequence) == n:
        res.append(copy.deepcopy(sequence))
        return
    if next_num <= n:
        stack.append(next_num)
        dfs(stack, sequence, next_num + 1)
        stack.pop()
    if stack:
        sequence.append(stack.pop())
        dfs(stack, sequence, next_num)
        stack.append(sequence.pop())


dfs(deque(), [], 1)

for e in res[::-1]:
    print(*e)