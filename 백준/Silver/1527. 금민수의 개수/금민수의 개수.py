A,B = map(int,input().split())
Q = [4,7]
ans = 0
while len(Q) > 1:
    F = Q[0]
    Q.pop(0)

    if F <= B:
        if A<=F:
            ans +=1
        Q.append(F*10+4)
        Q.append(F*10+7)

print(ans)