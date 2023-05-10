import sys

sys.setrecursionlimit(50000)


def func(start_y, start_x, width):
    global arr, number, flag
    if not flag:
        return
    if width == 1:
        if start_y == r and start_x == c:
            print(number)
            flag = False
        number += 1
        return
    next_width = width // 2
    if start_y <= r < start_y + next_width and start_x <= c < start_x + next_width:
        func(start_y, start_x, next_width)
    else:
        number += next_width * next_width
    if start_y <= r < start_y + next_width and start_x + next_width <= c < start_x + 2 * next_width:
        func(start_y, start_x + next_width, next_width)
    else:
        number += next_width * next_width
    if start_y + next_width <= r < start_y + 2 * next_width and start_x <= c < start_x + next_width:
        func(start_y + next_width, start_x, next_width)
    else:
        number += next_width * next_width
    if start_y + next_width <= r < start_y + 2 * next_width and start_x + next_width <= c < start_x + 2 * next_width:
        func(start_y + next_width, start_x + next_width, next_width)
    else:
        number += next_width * next_width


N, r, c = map(int, sys.stdin.readline().rstrip().split())
number = 0
flag = True
func(0, 0, 2 ** N)
