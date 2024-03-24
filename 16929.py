# 16929 Two Dots

import sys
sys.stdin = open("input/16929.txt", "r")

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isInBoard(y, x):
    return (0 <= y < n) and (0 <= x < m)

def isSameColor(ny, nx, y, x):
    return board[y][x] == board[ny][nx]

def isPrePoint(ny, nx, y, x):
    return (ny, nx) == (y, x)

def dfs(y, x, cnt, preY, preX):
    if visited[y][x] and cnt >= 4:
        return True
    visited[y][x] = True
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not isInBoard(ny, nx) or not isSameColor(ny, nx, y, x):
            continue
        if isPrePoint(ny, nx, preY, preX):
            continue
        if dfs(ny, nx, cnt + 1, y, x):
            return True
    return False

def isInCycle():
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(i, j, 1, -1, -1):
                    return True
    return False

print("Yes" if isInCycle() else "No")