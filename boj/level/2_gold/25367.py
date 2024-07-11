import sys
input = sys.stdin.readline

def cal_res():
    x, y = map(int, input().split())

    if (x - y) % 2 == 1 or ((x-y)//2 & y) > 0:
        print(0)
        return
    res = 1
    for i in range(58):
        bit = 1 << i
        if y & bit:
            res <<= 1
    print(res)

n = int(input())
for _ in range(n):
    cal_res()


# import sys

# input_num = int(input())

# for i in range(input_num):
#   x, y = map(int, sys.stdin.readline().split())
#   if (x - y) % 2 == 1 or ((x-y)//2 & y) > 0:
#     print(0)
#   else:
#     print(2**(y.bit_count()))

# 배운점
# a ^ b = a + b - 2 * (a & b)