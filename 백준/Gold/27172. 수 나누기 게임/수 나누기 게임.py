import sys
import math


def adjustScore():
    for p in range(1, bound // 2 + 1):
        if players[p] != -1:
            cur = p * 2
            while cur < bound:
                if players[cur] != -1:
                    score[players[p]] += 1
                    score[players[cur]] -= 1
                cur += p
    return


bound = 1000001
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
score = [0 for i in range(N)]
players = [-1 for _ in range(bound)]

for i in range(len(numbers)):
    players[numbers[i]] = i

adjustScore()

for i in score:
    print(i, end=' ')
