import sys
input = sys.stdin.readline


def parse_input():
    n = int(input())
    a = []
    b = []
    c = []
    d = []
    ab = []
    cd = []
    for _ in range(n):
        t1, t2, t3, t4 = map(int, input().split())
        a.append(t1)
        b.append(t2)
        c.append(t3)
        d.append(t4)
    for i in range(n):
        for j in range(n):
            ab.append(a[i] + b[j])
            cd.append(c[i] + d[j])
    return n, sorted(ab), sorted(cd)


n, ab, cd = parse_input()

ans = 0
start = 0
end = len(cd) - 1

while start < len(ab) and end >= 0:
    temp = ab[start] + cd[end]
    if temp == 0:
        ns = start + 1
        while ns < len(ab) and ab[start] == ab[ns]:
            ns += 1
        ne = end - 1
        while ne >= 0 and cd[end] == cd[ne]:
            ne -= 1
        ans += (ns - start) * (end - ne)
        start, end = ns, ne
    if temp < 0:
        start += 1
    if temp > 0:
        end -= 1

print(ans)
