import sys

i = 1
while True:
    L,P,V = map(int,sys.stdin.readline().rstrip().split())
    if L==0 and P==0 and V == 0:
        break
    sum = 0
    n1 = V//P
    sum += n1*L
    n2 = V%P
    sum += min(n2, L)
    print("Case %d: %d"%(i,sum))
    i+=1