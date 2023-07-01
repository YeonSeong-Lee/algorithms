import sys
input = sys.stdin.readline


def A_possible():
    return True


def B_possible(prev):
    if prev == 'B':
        return False
    return True


def C_possible(prev, pprev):
    if prev == 'C' or pprev == 'C':
        return False
    return True


def generate_attendance_record(A, B, C, prev, pprev):
    if A == 0 and B == 0 and C == 0:
        return ''

    if dp[A][B][C] != '':
        return dp[A][B][C]

    result = ''
    if A > 0 and A_possible():
        result = generate_attendance_record(A-1, B, C, 'A', prev)
        if result != -1:
            dp[A][B][C] = 'A' + result
            return dp[A][B][C]

    if B > 0 and B_possible(prev):
        result = generate_attendance_record(A, B-1, C, 'B', prev)
        if result != -1:
            dp[A][B][C] = 'B' + result
            return dp[A][B][C]

    if C > 0 and C_possible(prev, pprev):
        result = generate_attendance_record(A, B, C-1, 'C', prev)
        if result != -1:
            dp[A][B][C] = 'C' + result
            return dp[A][B][C]
    return -1


employees = input().strip()
A, B, C = employees.count('A'), employees.count('B'), employees.count('C')

# DP 테이블 초기화
dp = [[[''] * (C+1) for _ in range(B+1)] for _ in range(A+1)]

attendance_record = generate_attendance_record(A, B, C, '', '')
print(attendance_record)
