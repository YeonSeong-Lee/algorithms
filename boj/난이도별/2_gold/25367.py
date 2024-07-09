def cal_res():
    x, y = map(int, input().split())

    # s와 x의 차이가 홀수인지 검사합니다.
    # 홀수라면 조건을 만족하는 (a, b) 쌍이 존재할 수 없으므로 0을 출력하고 프로그램을 종료합니다.
    if (x - y) & 1:
        print(0)
        return

    # s와 x의 차이의 절반을 계산합니다. 이는 a와 b의 각 비트의 차이를 나타냅니다.
    a_and_b = int((x - y) / 2)

    # 결과를 저장할 변수를 초기화합니다.
    res = 1

    # 각 비트에 대해 처리를 수행합니다.
    for i in range(57):
        # i번째 비트가 1인 숫자를 생성합니다.
        bit = 1 << i

        # d의 i번째 비트가 1인지 검사합니다.
        if a_and_b & bit:
            if y & bit:
                res = 0
                break
        else:
            if y & bit:
                res <<= 1
    # 결과를 출력합니다.
    print(res)

# 입력을 받습니다.
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