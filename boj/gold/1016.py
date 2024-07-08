import sys
input = sys.stdin.readline

mi, ma = map(int, input().split())
max_root_plus_one = int(ma**0.5) + 1
ans = ma - mi + 1
no_squares = [True for _ in range(ans)]

for i in range(2, max_root_plus_one):
    sq = i * i
    for j in range((((mi-1)//sq)+1)*sq, ma+1, sq):
        if no_squares[j-mi]:
            ans -=1
            no_squares[j-mi] = False

print(ans)