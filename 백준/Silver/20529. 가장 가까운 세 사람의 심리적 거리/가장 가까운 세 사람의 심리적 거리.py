import math
import sys


def how_diff(elem1, elem2):
    num = 0
    for i in range(4):
        if elem1[i] != elem2[i]:
            num += 1
    return num


mbti = [['E', 'I'], ['N', 'S'], ['F', 'T'], ['P', 'J']]
mbti_list = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                mbti_list.append(mbti[0][i] + mbti[1][j] + mbti[2][k] + mbti[3][l])

dict = {i: {} for i in mbti_list}
for elem1 in mbti_list:
    for elem2 in mbti_list:
        dict[elem1][elem2] = how_diff(elem1, elem2)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    cnt = {i: 0 for i in mbti_list}
    N = int(sys.stdin.readline().rstrip())
    arr = list(sys.stdin.readline().rstrip().split())
    if N > 32:
        print(0)
    else:
        length = len(arr)
        min_val = math.inf
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    val = dict[arr[i]][arr[j]] + dict[arr[i]][arr[k]] + dict[arr[j]][arr[k]]
                    min_val = min(min_val, val)
        print(min_val if min_val != math.inf else 0)
