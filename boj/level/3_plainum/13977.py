import sys
input = sys.stdin.readline

MOD = 1_000_000_007
MAX = 4_000_000

# 팩토리얼과 팩토리얼의 모듈러 역원 계산
fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

# 팩토리얼 계산
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

# 최대 팩토리얼의 모듈러 역원 계산
inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)

# 나머지 팩토리얼의 모듈러 역원 계산
for i in range(MAX - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def binomial_coefficient(n, k):
    if k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD


m = int(input())
results = []
for _ in range(m):
    n, k = map(int, input().split())
    results.append(binomial_coefficient(n, k))

sys.stdout.write('\n'.join(map(str, results)) + '\n')

# LEARN:
# 페르마 소정리 (a^p-1 === 1 (mod p))를 이용해서 모률러 연산을 할 수 있도록 a^-1 을 얻어내기.
# 팩토리얼 미리 계산해두기, 연산을 그떄 그때 하면 시간이 오래걸림.
# https://www.youtube.com/watch?v=e7XnAlaD3TI
