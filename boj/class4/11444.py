import sys

def matrix_multiply(A, B, mod=1_000_000_007):
    """두 행렬 A와 B를 곱하고, 결과를 mod로 나눈 나머지를 반환합니다."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def matrix_power(matrix, n, mod=1_000_000_007):
    """행렬 matrix를 n번 거듭제곱하고, 결과를 mod로 나눈 나머지를 반환합니다."""
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result

def fibo(n):
    """행렬 거듭제곱을 사용하여 n번째 피보나치 수를 계산합니다."""
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    F_n = matrix_power(F, n-1)
    return F_n[0][0]

input = sys.stdin.readline
n = int(input())
print(fibo(n))