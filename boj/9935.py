# 9935 문자열 폭발

import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []
delimeter = bomb[-1]

for s in string:
    stack.append(s)
    if s == delimeter and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

print(''.join(stack) if stack else 'FRULA')
