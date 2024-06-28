import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(range(1, n+1))
store = []

def dfs():
    if len(store) == m:
        print(' '.join(map(str, store)))
        return

    for e in nums:
        if len(store) > 0 and e < store[-1]:
            continue
        store.append(e)
        dfs()
        store.pop()


dfs()
