import sys
from decimal import *

input = sys.stdin.readline

A, B, C = map(Decimal, input().split())
getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP
pi = Decimal(
    '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
err = Decimal('0.0000000000000000000000000000000000000000000001')


def sin_(x):
    tol = 0
    x = x % (Decimal("2") * pi)
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while abs(s-lasts) > err and tol < 1e10:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
        tol += 1
    return s


def f(x):
    return A * x + B * sin_(x) - C


def find_root():
    left, right = Decimal('0'), Decimal('200000')
    tol = 0
    while right - left > err and tol < 1000:
        mid = (left + right) / Decimal('2')
        if f(mid) > 0:
            right = mid
        else:
            left = mid
        tol += 1
    return (left + right) / 2


root = find_root()

print(f"{root:.6f}")

# LEARN
# 아주높은 정밀도... 소수 다루기