import sys

A,B = map(int, sys.stdin.readline().rstrip().split())
r = B
ans = -1
cnt = 1
while r>0:
    if r == A:
        ans = cnt
        break
    if r%2 == 0:
        r//=2
    elif r%10 == 1:
        r//=10
    else:
        break
    cnt+=1

print(ans)