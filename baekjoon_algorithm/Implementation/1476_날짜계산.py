import sys

E,S,M = map(int,sys.stdin.readline().rstrip().split())
n = 0

while True:
    A = n%15+1
    B = n%28+1
    C = n%19+1
    if A == E and B == S and C == M:
        break
    n+=1
print(n+1)
