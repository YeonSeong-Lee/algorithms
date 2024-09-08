def is_ppap_string(s):
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
            stack[-4:] = ['P']

    if stack == ['P']:
        return "PPAP"
    else:
        return "NP"

s = input().strip()
print(is_ppap_string(s))