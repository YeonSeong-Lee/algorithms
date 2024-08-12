import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

MOD = 1_000_000_007
ans = 0


powers_of_two = [1] * n
for i in range(1, n):
    powers_of_two[i] = (powers_of_two[i - 1] * 2) % MOD

for i in range(n):
    mi = nums[i] * powers_of_two[n - i - 1] % MOD
    ma = nums[i] * powers_of_two[i] % MOD
    ans = (ans + ma - mi) % MOD
# for i in range(n):
#     mi = nums[i] * pow(2, n-i-1, MOD)
#     ma = nums[i] * pow(2, i, MOD)
#     ans = (ans + ma - mi) % MOD
print(ans)

# LEARN
# MOD 연산, 파이썬 pow함수의 세번째 인자로 MOD받음, 덧셈이나 조합이 나오면 교환법칙을 생각해보기(==순서 상관없음. 몇번인지만 세면 됨.)
