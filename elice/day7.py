import sys

input = sys.stdin.readline

n, k = map(int, input().split())
CASE = 1 << 10
length = 10
dp = [[sys.maxsize] * CASE for _ in range(length + 1)]

if k == 10:
    print("1023456789")
    exit()

if k == 9:
    print("102345678")
    exit()

digit = [False] * 10
cnt = 0
while cnt != k:
    digit = [False] * 10
    cnt = 0
    n = str(int(n) + 1)
    for char in n:
        digit[int(char)] = True
    cnt = sum(digit)
print(n)

# 배운 점
# 걍 생구현으로 통과가 되는지 확인사항 잘 확인해보기