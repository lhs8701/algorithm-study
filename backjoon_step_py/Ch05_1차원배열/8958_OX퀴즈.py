import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    line = list(sys.stdin.readline().rstrip())
    comb = 0
    score = 0
    for elem in line:
        if elem == 'O':
            comb += 1
            score += comb
        else:
            comb = 0
    print(score)
