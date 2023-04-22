import sys


def back_tracking(level):
    global exit
    if level >= 81:
        for i in range(9):
            print("".join(map(str, row[i])))
        exit = True
        return
    if exit:
        return

    i = level // 9
    j = level % 9
    if matrix[i][j] != 0:
        back_tracking(level + 1)
    else:
        for num in range(1, 10):
            if num not in row[i] and num not in col[j] and num not in box[i // 3 * 3 + j // 3] and not exit:
                row[i][j] = num
                col[j][i] = num
                box[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] = num
                back_tracking(level + 1)
                row[i][j] = 0
                col[j][i] = 0
                box[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] = 0


matrix = []
row = [[] for _ in range(9)]
col = [[] for _ in range(9)]
box = [[] for _ in range(9)]

for i in range(9):
    temp = list(map(int, str(sys.stdin.readline().rstrip())))
    matrix.append(temp)
    for j in range(9):
        row[i].append(temp[j])
        col[j].append(temp[j])
        box[i // 3 * 3 + j // 3].append(temp[j])

exit = False
back_tracking(0)
