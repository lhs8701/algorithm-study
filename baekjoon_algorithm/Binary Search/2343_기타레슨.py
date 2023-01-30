import sys


def solve(lecture, N, M):
    pass


N, M = map(int, sys.stdin.readline().rstrip().split())
lecture = list(map(int, sys.stdin.readline().rstrip().split()))
print(solve)

if __name__ == "__main__":
    # test 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = 17
    result = solve(arr, 9, 3)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)