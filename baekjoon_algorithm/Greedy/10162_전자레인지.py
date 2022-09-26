import sys

T = int(sys.stdin.readline().rstrip())
button = [300,60,10]
num = [0,0,0]
for i in range(3):
    num[i]+=T//button[i]
    T%=button[i]
if T>0:
    print(-1)
else:
    print("%d %d %d"%(num[0],num[1],num[2]))