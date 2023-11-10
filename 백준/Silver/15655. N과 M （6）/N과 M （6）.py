n, m = map(int,input().split())

s = list(map(int,input().split()))

s.sort()

visited = [0]*(n)

temp = []

def solve(idx):
    global temp
    #만약 길이가 충족되면 print해줌
    if len(temp) == m:
        print(*temp)

    for i in range(idx,n):
        if s[i] not in temp:
            temp.append(s[i])
            solve(i+1)
            temp.pop()
solve(0)