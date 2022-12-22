import sys


def solve(numbers, N):
    ans = 0
    numbers.sort()

    for key in range(N):
        temp = numbers[:key] + numbers[key + 1:]
        low, high = 0, len(temp) - 1
        success = False
        while low < high:
            if temp[low] + temp[high] == numbers[key]:
                success = True
                break
            elif temp[low] + temp[high] > numbers[key]:
                high -= 1
            else:
                low += 1

        if success:
            ans += 1

    return ans


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
print(solve(numbers, N))

if __name__ == "__main__":
    # test1
    test = [0, 1, 2, 2, 5, 3, 4, 4]
    expected = 6
    result = solve(test, len(test))
    if result != expected:
        print("1, fail, ", result, ",", expected)

    # test2
    test = [0, 2, 2, 2, 2]
    expected = 4
    result = solve(test, len(test))
    if result != expected:
        print("2, fail,", result, ",", expected)

    # test3
    test = [-5, -2, -3]
    expected = 1
    result = solve(test, len(test))
    if result != expected:
        print("3, fail,", result, ",", expected)

    # test4
    test = [0, 0, 0]
    expected = 3
    result = solve(test, len(test))
    if result != expected:
        print("4, fail,", result, ",", expected)

    # test5
    test = [-5, -3, 0, 2, 2, 4]
    expected = 4
    result = solve(test, len(test))
    if result != expected:
        print("5, fail,", result, ",", expected)
