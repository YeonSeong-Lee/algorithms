from bisect import bisect_left, bisect_right
import sys
import math
input = sys.stdin.readline

n = int(input())
PRIME_NUM_RANGE = 10 ** 5
pn_bool = [True for _ in range(PRIME_NUM_RANGE + 1)]

for i in range(2, int(math.sqrt(PRIME_NUM_RANGE)) + 1):
    if pn_bool[i] == True:
        j = 2
        while i * j <= PRIME_NUM_RANGE:
            pn_bool[i * j] = False
            j += 1

prime_num = [i for i in range(2, PRIME_NUM_RANGE + 1) if pn_bool[i]]

sums = []


def f(a, b):
    min_prime_index = bisect_left(prime_num, a)
    max_prime_num_idx = bisect_right(prime_num, b)
    cnt = 1
    ans = 0
    for i in range(min_prime_index, max_prime_num_idx):
        if cnt % 2 == 1:
            ans += 3 * prime_num[i]
        else:
            ans -= prime_num[i]
        cnt += 1
    return ans


for _ in range(n):
    a, b = map(int, input().split())
    print(f(a, b))
