import sys
input = sys.stdin.readline

n, m = map(int, (input().split()))
pw = {}

for _ in range(n):
    site, cur_pw = input().split()
    pw[site] = cur_pw

for _ in range(m):
    print(pw[input().strip()])
