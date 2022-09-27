def collinearPoints(points):
    points.sort(key=lambda x: (x[0], x[1]))
    N = len(points)
    ans = []
    saved = []
    for v in range(N - 3):
        xv, yv = points[v][0], points[v][1]
        arr_gradient = []
        for i in range(v + 1, N):
            xi, yi = points[i][0], points[i][1]
            if xi - xv == 0:
                g = float('inf')
            else:
                g = (yi - yv) / (xi - xv)
            arr_gradient.append((xi, yi, g))
        arr_gradient.sort(key=lambda x: (x[2], x[0], x[1]))
        prev, comb = arr_gradient[0], 1
        size_arr = len(arr_gradient)
        for i in range(1, size_arr):
            if arr_gradient[i][2] == prev[2]:
                comb += 1
                if i == size_arr - 1 and comb >= 3 and arr_gradient[i] not in saved:
                    ans.append((xv, yv, arr_gradient[i][0], arr_gradient[i][1]))
                    saved.append(arr_gradient[i])
            else:
                if comb >= 3 and prev not in saved:
                    ans.append((xv, yv, prev[0], prev[1]))
                    saved.append(prev)
                comb = 1
            prev = arr_gradient[i]
    return ans


if __name__ == "__main__":
    print(
        collinearPoints([(19000, 10000), (18000, 10000), (32000, 10000), (21000, 10000), (1234, 5678), (14000, 10000)]))
    print(collinearPoints(
        [(10000, 0), (0, 10000), (3000, 7000), (7000, 3000), (20000, 21000), (3000, 4000), (14000, 15000),
         (6000, 7000)]))
    print(collinearPoints([(0, 0), (1, 1), (3, 3), (4, 4), (6, 6), (7, 7), (9, 9)]))
    print(collinearPoints([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (8, 0)]))
    print(collinearPoints([(7, 0), (14, 0), (22, 0), (27, 0), (31, 0), (42, 0)]))
    print(collinearPoints(
        [(12446, 18993), (12798, 19345), (12834, 19381), (12870, 19417), (12906, 19453), (12942, 19489)]))
    print(collinearPoints(
        [(1, 1), (2, 2), (3, 3), (4, 4), (2, 0), (3, -1), (4, -2), (0, 1), (-1, 1), (-2, 1), (-3, 1), (2, 1), (3, 1),
         (4, 1), (5, 1)]))
