import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ch_board = [[0]*N for _ in range(N)]

ch_board[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and ch_board[i][j] !=0:
            if i + board[i][j]<N:
                ch_board[i+board[i][j]][j] += ch_board[i][j]
            if j + board[i][j]<N:
                ch_board[i][j+board[i][j]] += ch_board[i][j]
print(ch_board[-1][-1])