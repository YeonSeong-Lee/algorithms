def is_ppap_string(s):
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
            stack[-4:] = ['P']  # "PPAP"를 "P"로 대체

    if stack == ['P']:
        return "PPAP"
    else:
        return "NP"


# 입력 받기
s = input().strip()
print(is_ppap_string(s))
