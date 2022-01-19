# import sys
#
# def getNextnum(i):
#     if i == 7:
#         return 0
#     else:
#         return i+1
# def getPrenum(i):
#     if i == 0:
#         return 7
#     else:
#         return i-1
#
# def rotate(idx, dir):
#     global l,r
#     if dir == 1:
#         l[idx] = getPrenum(l[idx])
#         r[idx] = getPrenum(r[idx])
#     else:
#         l[idx] = getNextnum(l[idx])
#         r[idx] = getNextnum(r[idx])
#
# gear = [[-1,-1,-1,-1,-1,-1,-1,-1]]
# comm = []
# l = [6]*5
# r = [2]*5
# score = 0
#
# for i in range(4):
#     gear.append(list(sys.stdin.readline().rstrip()))
#
# K = int(sys.stdin.readline().rstrip())
# backup = 0
# for i in range(K):
#     idx, d = map(int, sys.stdin.readline().rstrip().split())
#     dir = d
#     backup = gear[idx][l[idx]]
#     for j in range(idx-1,0,-1):
#         a = gear[j][r[j]]
#         if a == backup:
#             break
#         else:
#             backup = gear[j][l[j]]
#             dir *= -1
#             rotate(j,dir)
#     dir = d
#     backup = gear[idx][r[idx]]
#     for j in range(idx+1,5):
#         a = gear[j][l[j]]
#         if a == backup:
#             break
#         else:
#             backup = gear[j][r[j]]
#             dir *= -1
#             rotate(j,dir)
#     rotate(idx,d)
# for i in range(1,5):
#     if gear[i][getPrenum(getPrenum(r[i]))] == '1':
#         score+=2**(i-1)
#
# print(score)
#

import sys
from collections import deque

gear = [[-1,-1,-1,-1,-1,-1,-1,-1]]
score = 0
deq = [0]
for i in range(4):
    gear.append(list(sys.stdin.readline().rstrip()))
    temp = deque([0,1,2,3,4,5,6,7])
    deq.append(temp)

K = int(sys.stdin.readline().rstrip())
backup = 0
for i in range(K):
    idx, d = map(int, sys.stdin.readline().rstrip().split())

    dir = d
    backup = gear[idx][deq[idx][6]]
    for j in range(idx-1,0,-1):
        a = gear[j][deq[j][2]]
        if a == backup:
            break
        else:
            backup = gear[j][deq[j][6]]
            dir *= -1
            deq[j].rotate(dir)
    dir = d
    backup = gear[idx][deq[idx][2]]
    for j in range(idx+1,5):
        a = gear[j][deq[j][6]]
        if a == backup:
            break
        else:
            backup = gear[j][deq[j][2]]
            dir *= -1
            deq[j].rotate(dir)
    deq[idx].rotate(d)
for i in range(1,5):
    if gear[i][deq[i][0]] == '1':
        score+=2**(i-1)

print(score)

