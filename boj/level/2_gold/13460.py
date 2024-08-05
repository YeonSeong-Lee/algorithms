# LEARN
#  방향에 매몰되지 말고, 거리를 통해서 판별하기
#  visited를 꼭 리스트로 안 만들어도됨. set으로 간편하게

from collections import deque


def move(y, x, dy, dx, board):
    move_count = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        move_count += 1
    return y, x, move_count


def bfs(board, n, m, ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0))
    visited = set()
    visited.add((ry, rx, by, bx))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        ry, rx, by, bx, depth = q.popleft()

        if depth >= 10:
            return -1

        for dy, dx in directions:
            nry, nrx, r_moves = move(ry, rx, dy, dx, board)
            nby, nbx, b_moves = move(by, bx, dy, dx, board)

            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                return depth + 1

            if nry == nby and nrx == nbx:
                if r_moves > b_moves:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            if (nry, nrx, nby, nbx) not in visited:
                visited.add((nry, nrx, nby, nbx))
                q.append((nry, nrx, nby, nbx, depth + 1))

    return -1


def solve():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    ry = rx = by = bx = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ry, rx = i, j
            elif board[i][j] == 'B':
                by, bx = i, j

    result = bfs(board, n, m, ry, rx, by, bx)
    print(1 if result != -1 else 0)


if __name__ == "__main__":
    solve()
