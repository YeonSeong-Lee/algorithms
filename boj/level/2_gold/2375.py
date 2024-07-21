import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
# TODO: 전형적인 세그먼트 트리 풀고 다시 와보기
# https://www.acmicpc.net/problem/2042



for _ in range(m):
    a, b = map(int, input().split())