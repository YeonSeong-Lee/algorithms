import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
res = 0

def count_case(shape):
    cnt = 0
    for e in shape:
        y, x = e
        if y < 0 or y >= n or x < 0 or x >= m:
            return 0
        cnt += info[y][x]
    return cnt


def max_count(i, j):
    # - block
    case_1 = count_case([(i, j), (i+1, j), (i+2, j), (i+3, j)])
    case_2 = count_case([(i, j), (i, j+1), (i, j+2), (i, j+3)])
    # ㅁ block
    case_3 = count_case( [(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
    # L block 세로
    case_4 = count_case([(i, j), (i+1, j), (i+2, j), (i+2, j+1)])
    case_5 = count_case([(i, j), (i+1, j), (i+2, j), (i+2, j-1)])
    case_6 = count_case([(i, j), (i, j+1), (i+1, j+1), (i+2, j+1)])
    case_7 = count_case([(i, j), (i, j+1), (i+1, j), (i+2, j)])
    # L block 가로
    case_8 = count_case([(i, j), (i, j+1), (i, j+2), (i+1, j+2)])
    case_9 = count_case([(i, j), (i, j+1), (i, j+2), (i-1, j+2)])
    case_10 = count_case([(i, j), (i+1, j), (i+1, j+1), (i+1, j+2)])
    case_11 = count_case([(i, j), (i+1, j), (i, j+1), (i, j+2)])
    # S block
    case_12 = count_case([(i, j), (i+1, j), (i+1, j+1), (i+2, j+1)])
    case_13 = count_case([(i, j), (i+1, j), (i+1, j-1), (i+2, j-1)])
    case_14 = count_case([(i, j), (i, j+1), (i-1, j+1), (i-1, j+2)])
    case_15 = count_case([(i, j), (i, j+1), (i+1, j+1), (i+1, j+2)])
    # ㅗ block
    case_16 = count_case([(i, j), (i+1, j), (i-1, j), (i, j+1)])
    case_17 = count_case([(i, j), (i+1, j), (i-1, j), (i, j-1)])
    case_18 = count_case([(i, j), (i, j+1), (i, j-1), (i+1, j)])
    case_19 = count_case([(i, j), (i, j+1), (i, j-1), (i-1, j)])

    return max(case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9, case_10, case_11, case_12, case_13, case_14, case_15, case_16, case_17, case_18, case_19)


for _ in range(n):
    line = list(map(int, input().split()))
    info.append(line)

for i in range(n):
    for j in range(m):
        res = max(max_count(i, j), res)

print(res)
