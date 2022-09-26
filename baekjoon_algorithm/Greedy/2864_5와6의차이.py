import sys

A, B = sys.stdin.readline().rstrip().split()
maxA, minA = list(A), list(A)
maxB, minB = list(B), list(B)
sizeA, sizeB = len(A), len(B)
for i in range(sizeA):
    if maxA[i] == '5':
        maxA[i] = '6'
    if minA[i] == '6':
        minA[i] = '5'

for i in range(sizeB):
    if maxB[i] == '5':
        maxB[i] = '6'
    if minB[i] == '6':
        minB[i] = '5'

print(int("".join(minA)) + int("".join(minB)), int("".join(maxA)) + int("".join(maxB)))
