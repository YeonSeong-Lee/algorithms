import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
people = []
stack = deque()

def is_small_than(a, b):
    a_alphabet, a_num = a.split('-')
    b_alphabet, b_num = b.split('-')
    if a_alphabet == b_alphabet:
        return int(a_num) < int(b_num)
    else:
        return a_alphabet < b_alphabet

for _ in range(n):
    line = input().split()
    for e in line:
        people.append(e)
last = '-'

for e in people:
    while stack and is_small_than(stack[-1], e):
        if is_small_than(stack[-1], last):
            print("BAD")
            exit()
        last = stack.pop()
    stack.append(e)

while stack:
    if is_small_than(last, stack[-1]):
        last = stack.pop()
    else:
        print("BAD")
        exit()

print("GOOD")
