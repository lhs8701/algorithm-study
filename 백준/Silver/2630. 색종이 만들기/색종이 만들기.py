import sys


def func(start_y, start_x, width):
    if check(start_y, start_x, width):
        count[matrix[start_y][start_x]] += 1
        return
    half_width = width // 2
    func(start_y, start_x, half_width)
    func(start_y, start_x + half_width, half_width)
    func(start_y + half_width, start_x, half_width)
    func(start_y + half_width, start_x + half_width, half_width)


def check(y, x, width):
    color = matrix[y][x]
    for i in range(y, y + width):
        for j in range(x, x + width):
            if matrix[i][j] != color:
                return False
    return True


N = int(sys.stdin.readline().rstrip())
matrix = []
count = [0, 0]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

func(0, 0, N)
print(count[0])
print(count[1])
