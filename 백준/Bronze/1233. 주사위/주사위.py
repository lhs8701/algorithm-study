a = list(map(int, input().split()))
ch = [0] * (20 + 20 + 40 + 1)
for i in range(1, a[0]+1):
    for j in range(1, a[1]+1):
        for k in range(1, a[2]+1):
            ch[i+j+k] += 1
            
for i in range(len(ch)):
    if ch[i] == max(ch):
        print(i)
        break