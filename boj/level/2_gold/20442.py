import sys
input = sys.stdin.readline

# KKRKK -> 5

s = input().strip()
ans = 0
n = len(s)

left_ks = [0] * n
right_ks = [0] * n
r_index = []

cnt = 0
for i in range(n):
    if s[i] == 'R':
      r_index.append(i)
    left_ks[i] = cnt
    if s[i] == 'K':
      cnt += 1

cnt = 0
for i in range(n-1, -1, -1):
  right_ks[i] = cnt
  if s[i] == 'K':
    cnt += 1

ans = 0
left = 0
right = len(r_index) - 1
while left <= right:
    k_count = min(left_ks[r_index[left]], right_ks[r_index[right]])
    ans = max(ans, right - left + 1 + k_count * 2)
    if left_ks[r_index[left]] > right_ks[r_index[right]]:
      right -= 1
    else:
      left += 1

print(ans)