
N = int(input())
listA = list(map(int,input().split()))
listB = list(map(int,input().split()))

listA.sort()
listA.reverse()
listB.sort()
sum = 0
for i in range(N):
    sum+=listA[i]*listB[i]

print(sum)