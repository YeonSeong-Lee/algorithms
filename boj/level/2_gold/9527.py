import sys

input = sys.stdin.readline

a, b = map(int, input().split())


def count_one_untill_(n):
    cnt = 0
    bi = bin(n)[2:]
    for i in range(len(bi) - 1, -1, -1):
        digit = 1 << (i + 1)
        half_digit = 1 << i
        quotient = (n + 1) // digit
        remainder = (n + 1) % digit
        cnt += quotient * half_digit
        if remainder > half_digit:
            cnt += remainder - half_digit
    return cnt


print(count_one_untill_(b) - count_one_untill_(a - 1))
