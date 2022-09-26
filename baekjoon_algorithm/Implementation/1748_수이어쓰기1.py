import sys

N = sys.stdin.readline().rstrip()
n = len(N)
sum = 0
d = 1

while d<n:
    sum+=d*9*(10**(d-1))
    d+=1

sum+=n*(int(N)-10**(d-1)+1)
print(sum)
