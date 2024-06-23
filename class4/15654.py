import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
store = []


def dfs():
    if len(store) == m:
        print(' '.join(map(str, store)))
        return

    for e in nums:
        if e in store:
            continue
        store.append(e)
        dfs()
        store.pop()


dfs()
