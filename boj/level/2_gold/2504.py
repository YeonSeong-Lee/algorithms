import sys
input = sys.stdin.readline

s = input().strip()
ans = 0
temp = 1
stack = []
for i, e in enumerate(s):
    if e == '(':
        temp *= 2
        stack.append(e)
    if e == '[':
        temp *= 3
        stack.append(e)
    if e == ')':
        if i > 0 and s[i-1] == '(':
            ans += temp
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        temp //= 2
        stack.pop()
    if e == ']':
        if i > 0 and s[i-1] == '[':
            ans += temp
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        temp //= 3
        stack.pop()

if stack:
    print(0)
    exit()
print(ans)

# LEARN
# 덧셈에서는 기준점을 다르게 볼 수도 있음. 곱셈의 분배법칙!
