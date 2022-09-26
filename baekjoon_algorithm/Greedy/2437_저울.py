import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
jew = []
bag = []
for i in range(N):
    M,V = map(int,sys.stdin.readline().rstrip().split())
    jew.append((M,V))
for i in range(K):
    bag.append(int(sys.stdin.readline().rstrip()))

bag.sort()
jew.sort(key=lambda x:-x[1])
print(bag)
print(jew)
sum = 0
for i in range(N):
    cur = jew[i]
    for j in range(K):
        if cur[0] <= bag[j]:
            bag[j] = -1
            sum+=cur[1]
print(sum)