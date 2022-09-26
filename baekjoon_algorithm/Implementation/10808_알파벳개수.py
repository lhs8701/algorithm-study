import sys
S = list(sys.stdin.readline().rstrip())

alpha = [0]*26
for i in range(len(S)):
    alpha[ord(S[i]) - ord('a')]+=1
for i in alpha:
    print(i, end=" ")