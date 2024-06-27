import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()
pnl = 2 * n + 1

def next_idx(i):
    for idx in range(pnl):
        if idx % 2 == 0:
            if s[i + idx] != 'I':
                return i + idx + 1
        else:
            if s[i + idx] != 'O':
                return i + idx
    return -1

cnt = 0
flag = 0
i = 0
while (i < m):
    if flag == 0:
        if i + pnl > m:
            break
        pn_idx = next_idx(i)
        if pn_idx != -1:
            i = pn_idx
        else:
            cnt += 1
            flag = 1
    else:
        if i + pnl + 1 >= m:
            break
        if s[i + pnl] == 'O' and s[i + pnl + 1] == 'I':
            cnt +=1
            i += 2
        else:
            flag = 0
            i += 2

print(cnt)
