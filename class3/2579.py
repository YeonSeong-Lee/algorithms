import sys
input = sys.stdin.readline

n = int(input())
score = [0] * 301
staris = [0] * 301

for i in range(1, n+1):
    staris[i] = int(input())
score[1] = staris[1]
score[2] = staris[2]
# TODO: 다시풀기, 맨처음 조건들이 어디까지 갈지 생각해보기. 이 경우는 3까지 초기값임.


print(score[n])
