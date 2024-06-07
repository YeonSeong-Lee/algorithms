import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
    half = 1 << n-1
    if (r < half and c < half):
        return z(n-1, r, c)
    elif (r < half and c >= half):
        return half ** 2 + z(n-1, r, c - half)
    elif (r >= half and c < half):
        return 2 * half ** 2 + z(n-1, r - half, c)
    else:
        return 3 * half ** 2 + z(n-1, r - half, c - half)

print(z(n, r, c))