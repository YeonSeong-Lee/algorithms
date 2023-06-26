# 1043 거짓말

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]

for _ in range(M):
    for i in range(len(party)):
        if set(truth) & set(party[i]):
            truth += party[i]
            party.pop(i)
            break

print(len(party))
