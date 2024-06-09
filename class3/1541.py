data = input().split('-')

ans = 0
for i, e in enumerate(data):
    temp = sum(list(map(int, e.split('+'))))
    if i == 0:
        ans += temp
    else:
        ans -= temp

print(ans)
