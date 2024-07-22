import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = sys.maxsize
    a = b = c = 0
    nums.sort()

    for i in range(n-2):
        start = i + 1
        end = n - 1
        while start < end:
            sum_tree = nums[start] + nums[end] + nums[i]
            if start == i or end == i:
                if sum_tree < 0:
                    start += 1
                else:
                    end -= 1
                continue
            temp = abs(sum_tree)
            if temp < ans:
                a = nums[start]
                b = nums[end]
                c = nums[i]
                ans = temp
            if sum_tree < 0:
                start += 1
            else:
                end -= 1
    print(*sorted([a, b, c]))

main()