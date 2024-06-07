import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = len(a) - 1
    j = len(b) - 1
    ans = 0
    while i > 0:
        while a[i] <= b[j] and j > 0:
            j += -1
        if a[i] > b[j]:
            ans += j + 1
        i += -1
    print("ans :", ans)
