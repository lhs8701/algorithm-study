import sys

N = int(sys.stdin.readline().rstrip())
alpha = [0]*26
num=9
sum=0
for i in range(N):
    t = list(sys.stdin.readline().rstrip())
    t.reverse()
    for j in range(len(t)):
        n = ord(t[j]) - ord('A')
        alpha[n] += 10**j

alpha.sort(reverse=True)
for i in range(len(alpha)):
    if alpha[i] == 0:
        break
    sum+=alpha[i]*num
    num-=1

print(sum)

