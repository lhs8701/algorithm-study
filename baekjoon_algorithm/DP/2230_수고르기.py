import sys


def solve(arr, M):
    N = len(arr)
    arr.sort()
    left, right = 0, 0
    result = sys.maxsize
    while left <= right and right < N:
        var = arr[right] - arr[left]
        if var < M:
            right += 1
        elif var == M:
            return var
        else:
            result = min(result, var)
            left += 1
    return result


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

print(solve(arr, M))

if __name__ == "__main__":
    # test 1
    arr = [1, 2, 3, 4, 5]
    M = 1
    expected = 1
    result = solve(arr, M)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)

    # test 2
    arr = [1, 3, 5]
    M = 3
    expected = 4
    result = solve(arr, M)
    if result != expected:
        print("test 2 fail, result:", result, ", expected:", expected)

    # test 3
    arr = [1, 2, 3, 3]
    M = 0
    expected = 0
    result = solve(arr, M)
    if result != expected:
        print("test 3 fail, result:", result, ", expected:", expected)

    # test 4
    arr = [1, 2, 2, 4]
    M = 0
    expected = 0
    result = solve(arr, M)
    if result != expected:
        print("test 4 fail, result:", result, ", expected:", expected)
