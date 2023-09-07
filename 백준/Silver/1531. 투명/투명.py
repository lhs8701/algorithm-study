n,m= map(int,input().split())
board = [[0]*100 for x in range(100)]
for k in range(n):
    xi, yi, xf, yf = map(int, input().split())
    for i in range(xi, xf+1):
        for j in range(yi, yf+1):
            board[i-1][j-1] += 1
count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > m:
            count += 1
print(count)