import sys

n = int(sys.stdin.readline().rstrip())
coin = [500,100,50,10,5,1]

sum = 0
N = 1000-n
for i in coin:
    sum+=N//i
    N%=i

print(sum)