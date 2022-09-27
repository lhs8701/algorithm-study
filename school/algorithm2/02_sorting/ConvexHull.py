import math


def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0:
        return True
    else:
        return False


def grahamScan(points):
    # 1. 기준점 P 탐색
    p_arr = sorted(points, key=lambda x: (x[1], -x[0]))
    px, py = p_arr[0]
    del p_arr[0]

    # 2. P와의 각도 기준 정렬
    radian_arr = []
    for a in p_arr:
        ax, ay = a[0], a[1]
        r = math.atan2(ay - py, ax - px)
        radian_arr.append((ax, ay, r))
    p_arr = sorted(radian_arr, key=lambda x: x[2])
    # 3. stack 초기화
    stack = []
    stack.insert(0, (px, py))
    stack.insert(0, (p_arr[0][0], p_arr[0][1]))
    del p_arr[0]

    # 4. for loop
    for elem in p_arr:
        k = (elem[0], elem[1])
        stack.insert(0, k)
        while len(stack) >= 3:
            k = stack.pop(0)
            j = stack.pop(0)
            i = stack.pop(0)
            if ccw(i, j, k):
                stack.insert(0, i)
                stack.insert(0, j)
                stack.insert(0, k)
                break
            else:
                stack.insert(0, i)
                stack.insert(0, k)

    # 5. stack 역순 리스트 반환
    stack.reverse()

    return stack


if __name__ == "__main__":
    print(grahamScan([(0, 0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-4, -1)]))
    print(grahamScan(
        [(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1), (-2, -1), (-2, -3), (-3, 3), (-4, 0), (-4, -2),
         (-4, -4)]))
