import sys
input = sys.stdin.readline

ppap = input().strip()
stack = []
flag = False

if len(ppap) == 1 and ppap[0] == 'P':
    print("PPAP")
    exit()

if len(ppap) == 2 or 'A' not in ppap:
    print("NP")
    exit()

for e in ppap:
    if flag == True and e == 'P':
        flag = False
    if flag == True and e == 'A':
        print("NP")
        exit()
    stack.append(e)
    if stack[-1] == 'A':
        if len(stack) <= 2:
            print("NP")
            exit()
        flag = True
        stack.pop()  # A삭제
        temp1 = stack.pop()
        temp2 = stack.pop()
        if temp1 != 'P' or temp2 != 'P':
            print("NP")
            exit()

if flag or stack[-1] == 'A' or len(stack) > 2:
    print("NP")
else:
    print("PPAP")
