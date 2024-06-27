import sys
input = sys.stdin.readline

def is_all_same_color(n, r, c, color):
    flag = True
    for i in range(r, n+r):
        for j in range(c, n+c):
            if int(info[i][j]) != color:
                flag = False
                return flag
    return flag

def count_color(n, r, c, color):
    if is_all_same_color(n, r, c, color):
        return 1
    if n == 1:
        return 0
    half = n // 2
    res = count_color(half, r, c, color)
    res += count_color(half, r + half, c, color)
    res += count_color(half, r, c + half, color)
    res += count_color(half, r + half, c + half, color)
    return res

info = []
n = int(input())
for _ in range(n):
    info.append(input().split())

print(count_color(n, 0, 0, 0))
print(count_color(n, 0, 0, 1))
