import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
board_b = []
board_w = []
for i in range(8):
    if i % 2 == 0:
        board_b.append(black)
        board_w.append(white)
    else:
        board_b.append(white)
        board_w.append(black)


def func(x, y, board_8):
    global board
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != board_8[i][j]:
                cnt += 1
    return cnt


ans = sys.maxsize
for i in range(0, N - 7):
    for j in range(0, M - 7):
        ans = min(ans, func(i, j, board_b), func(i, j, board_w))

print(ans)
