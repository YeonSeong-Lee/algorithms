import sys
from itertools import combinations

input = sys.stdin.readline

# 입력 처리
s = input().strip()

# 괄호 쌍 찾기
stack = []
pairs = []
for i, char in enumerate(s):
    if char == '(':
        stack.append(i)
    elif char == ')':
        start = stack.pop()
        pairs.append((start, i))

# 괄호 제거
results = set()
for i in range(1, len(pairs) + 1):
    for comb in combinations(pairs, i):
        temp = list(s)
        for start, end in comb:
            temp[start] = ''
            temp[end] = ''
        results.add(''.join(temp))

# 중복 제거 및 정렬
results = sorted(results)

# 결과 출력
for result in results:
    print(result)

# LEARN
# 문자열 지우기 테크닉!