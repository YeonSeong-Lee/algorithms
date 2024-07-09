import sys
input = sys.stdin.readline

s = input().strip()
x = 0
y = 0
lv = len(s)

for i in range(lv, 0, -1):
    if s[len(s) - i] == '0':
        continue
    if s[len(s) - i] == '1':
        x += 2 ** (i - 1)
    elif s[len(s) - i] == '2':
        y += 2 ** (i - 1)
    else:
        x += 2 ** (i - 1)
        y += 2 ** (i - 1)

print(len(s), x, y)
