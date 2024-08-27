import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
nums = input().strip()
stack = deque()
origin_k = int(k)
for e in nums:
    while stack and k > 0 and stack[-1] < e:
        stack.pop()
        k -= 1
    stack.append(e)

stack = list(stack)
print(''.join(stack[:n-origin_k]))

# LEARN
# 스택, 모노스택 알고리즘에 조금의 응용을 하면 됨.
# 마지막에 빼야하는걸 다 못 빼는 경우가 생길 수 있으니 유의
