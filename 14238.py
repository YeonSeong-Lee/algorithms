import sys
input = sys.stdin.readline


def generate_attendance_record(A, B, C, prev, pprev):
    if A == 0 and B == 0 and C == 0:
        print(''.join(answer))
        exit(0)

    if dp[A][B][C][prev][pprev]:
        return False

    dp[A][B][C][prev][pprev] = True

    if A > 0:
        answer[A + B + C - 1] = 'A'
        if generate_attendance_record(A-1, B, C, a, prev):
            return True

    if B > 0 and prev != 1:
        answer[A + B + C - 1] = 'B'
        if generate_attendance_record(A, B-1, C, b, prev):
            return True

    if C > 0 and prev != c and pprev != c:
        answer[A + B + C - 1] = 'C'
        if generate_attendance_record(A, B, C-1, c, prev):
            return True
    return False


employees = input().strip()
A, B, C = employees.count('A'), employees.count('B'), employees.count('C')
a, b, c = 0, 1, 2
answer = [''] * (len(employees))

# DP 테이블 초기화
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(
    C+1)] for _ in range(B+1)] for _ in range(A+1)]

attendance_record = generate_attendance_record(A, B, C, 0, 0)
print(-1)
