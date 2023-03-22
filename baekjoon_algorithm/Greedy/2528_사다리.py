import math
import sys


def is_overlap(n1, n2):
    return (stair[n1][0] <= stair[n2][0] and stair[n2][0] <= stair[n1][1]) or (stair[n1][0] >= stair[n2][0] and stair[n1][0] <= stair[n2][1])


def calculate(n1, n2):
    if stair[n1][0] > stair[n2][0]:
        n1, n2 = n2, n1
    dir1 = stair[n1][2]
    dir2 = stair[n2][2]

    if dir1 == dir2:
        if dir1 == 1:
            t = min(stair[n1][0], stair[n2][0]) - 0
        else:
            t = L - max(stair[n1][1], stair[n2][1])
        return math.ceil((stair[n2][0] - stair[n1][1]) / 2) + t
    else:
        if dir1 == 0 and dir2 == 1:
            return math.ceil((stair[n2][0] - stair[n1][1]) / 2)
        else:
            if stair[n1][0] < L - stair[n2][1]:
                diff = (L - stair[n2][1]) - stair[n1][0]
                new_1 = (0 + diff, stair[n1][1] - stair[n1][0] + diff)
                new_2 = (stair[n2][0] + (L - stair[n2][1]), L)
            else:
                diff = stair[n1][0] - (L - stair[n2][1])
                new_1 = (0, stair[n1][1] - stair[n1][0])
                new_2 = (stair[n2][0] + (L - stair[n2][1]) - diff, L - diff)
            return math.ceil((new_2[0] - new_1[1]) / 2)


def renew(n, time, L):
    time %= L
    dir = stair[n][2]
    l = stair[n][1] - stair[n][0]
    flag = L - l
    end_of_start = L - l - stair[n][0]
    if dir == 0:
        if stair[n][0] + time < flag:
            stair[n][0] += time
            stair[n][1] += time
        else:
            stair[n][0] += end_of_start - (time - end_of_start)
            stair[n][1] += end_of_start - (time - end_of_start)
    else:
        if stair[n][0] - time >= 0:
            stair[n][0] -= time
            stair[n][1] -= time
        else:
            stair[n][0] += end_of_start - (time - end_of_start)
            stair[n][1] += end_of_start - (time - end_of_start)
    if time >= flag:
        stair[n][2] = 1 - stair[n][2]


N, L = map(int, sys.stdin.readline().rstrip().split())
stair = [[0, 0, 0] for i in range(N)]
ans = 0
for i in range(N):
    l, d = map(int, sys.stdin.readline().rstrip().split())
    if d == 0:
        stair[i][0] = 0
        stair[i][1] = l
    else:
        stair[i][0] = L - l
        stair[i][1] = L
    stair[i][2] = d

print(stair)
for i in range(N - 1):
    if is_overlap(i, i + 1):
        continue
    time = calculate(i, i + 1)
    for j in range(i + 1, N):
        renew(j, time, L)
    ans += time
print(ans)
