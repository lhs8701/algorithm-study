import sys

def draw():
    global n
    x = y = n//2
    cnt = num = 2
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    t = 0
    board[x][y] = 1; x-=1; y-=1

    while True:
        for _ in range(4):
            a,b = d[t]
            for _ in range(cnt):
                x+=a; y+=b
                board[x][y] = num
                if num==m:
                    ans[0]=x+1; ans[1]=y+1
                if num==n**2:
                    return
                num+=1
            t = (t+1)%4
        cnt+=2
        x-=1; y-=1

n = int(input())
m = int(input())
board = [[0]*n for _ in range(n)]
ans = [n//2+1,n//2+1]
draw()
for i in board:
    print(*i)
print(*ans)