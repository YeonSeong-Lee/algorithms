import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
mid = (start + end)//2
res = 0

def amount_tree(h):
    total = 0
    for e in trees:
        if e > h:
            total += e - h
    return total

while start <= end:
    mid = (start + end) // 2
    if amount_tree(mid) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
