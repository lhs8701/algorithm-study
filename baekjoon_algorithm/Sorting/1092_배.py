import sys


def solve(crane, box):
    N = len(crane)
    M = len(box)
    crane.sort(key=lambda x: x)
    box.sort(key=lambda x: -x)
    if crane[-1] < box[0]:
        return -1

    arr = [[i, 0] for i in crane]
    for i in range(M):
        weight = box[i]
        for j in range(N):
            if weight > arr[j][0]:
                continue
            cur = j
            while cur < N - 1 and arr[cur][1] == arr[cur + 1][1]:
                cur += 1
            arr[cur][1] += 1
            break

    return arr[-1][1]


# N = int(sys.stdin.readline().rstrip())
# crane = list(map(int, sys.stdin.readline().rstrip().split()))
# M = int(sys.stdin.readline().rstrip())
# box = list(map(int, sys.stdin.readline().rstrip().split()))
# print(solve(crane, box))

if __name__ == "__main__":

    # test 1
    test_crane = [6, 8, 9]
    test_box = [2, 5, 2, 4, 7]
    expected = 2
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 1 fail | result:", result, "| expected:", expected)

    # test 2
    test_crane = [19, 20]
    test_box = [14, 12, 16, 19, 16, 1, 5]
    expected = 4
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 2 fail | result:", result, "| expected:", expected)

    # test 3
    test_crane = [23, 32, 25, 28]
    test_box = [5, 27, 10, 16, 24, 20, 2, 32, 18, 7]
    expected = 3
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 3 fail | result:", result, "| expected:", expected)

    # test 4
    test_crane = [11, 17, 5, 2, 20, 7, 5, 5, 20, 7]
    test_box = [18, 18, 15, 15, 17]
    expected = 2
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 4 fail | result:", result, "| expected:", expected)

    # test 5
    test_crane = [5, 5, 5]
    test_box = [7, 7]
    expected = -1
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 5 fail | result:", result, "| expected:", expected)

    # test 6
    test_crane = [1, 2, 3, 4]
    test_box = [1, 1, 2, 2, 3, 3, 4, 4]
    expected = 2
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 6 fail | result:", result, "| expected:", expected)

    # test 7
    test_crane = [10, 6, 5]
    test_box = [6, 8, 9, 6, 8, 6, 9, 6, 8, 6, 9]
    expected = 6
    result = solve(test_crane, test_box)
    if result != expected:
        print("test 7 fail | result:", result, "| expected:", expected)
