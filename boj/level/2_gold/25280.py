import sys
input = sys.stdin.readline


def calculate_win_probability(time, intervals):
    win_prob = 1
    for a, b in intervals:
        if time > b:
            return 0
        elif a < time < b:
            win_prob *= (b - time) / (b - a)
    return win_prob


def find_max_time(intervals):
    low, high = 0, 100000
    while high - low > 1e-9:
        mid = (low + high) / 2
        if calculate_win_probability(mid, intervals) >= 0.5:
            low = mid
        else:
            high = mid
    return low


N = int(input().strip())
intervals = []
for _ in range(N):
    a, b = map(float, input().strip().split())
    intervals.append((a, b))

result = find_max_time(intervals)
print(result)

