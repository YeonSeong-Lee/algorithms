import sys
input = sys.stdin.readline


def A_possible():
    return True


def B_possible(record):
    if len(record) < 1:
        return True
    if record[-1] == 'B':
        return False
    return True


def C_possible(record):
    if len(record) < 2:
        return True
    if record[-1] == 'C' or record[-2] == 'C':
        return False
    return True


def generate_attendance_record(A, B, C, record, dp):
    if A == 0 and B == 0 and C == 0:
        return ''.join(record)

    if dp[A][B][C] != '':
        return dp[A][B][C]

    if A > 0 and A_possible():
        record.append('A')
        result = generate_attendance_record(A-1, B, C, record, dp)
        if result != -1:
            dp[A][B][C] = result
            return result
        record.pop()

    if B > 0 and B_possible(record):
        record.append('B')
        result = generate_attendance_record(A, B-1, C, record, dp)
        if result != -1:
            dp[A][B][C] = result
            return result
        record.pop()

    if C > 0 and C_possible(record):
        record.append('C')
        result = generate_attendance_record(A, B, C-1, record, dp)
        if result != -1:
            dp[A][B][C] = result
            return result
        record.pop()

    return -1


employees = list(input().strip())
A, B, C = employees.count('A'), employees.count('B'), employees.count('C')

# DP 테이블 초기화
dp = [[[''] * (C+1) for _ in range(B+1)] for _ in range(A+1)]

attendance_record = generate_attendance_record(A, B, C, [], dp)
print(attendance_record)
