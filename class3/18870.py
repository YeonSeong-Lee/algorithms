import sys
input = sys.stdin.readline

n = int(input())
xs = list(map(int, input().split()))



sorted_xs = sorted(set(xs))
sorted_dict = {}

for i, v in enumerate(sorted_xs):
    sorted_dict[v] = i

for _ in xs:
    print(sorted_dict[_], end=' ')

