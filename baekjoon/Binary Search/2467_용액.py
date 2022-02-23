import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

solution1 = 0
solution2 = 0
solution_val = sys.maxsize
left = 0
right = len(arr) - 1

while left < right:
    value = abs(arr[left] + arr[right])
    if solution_val > value:
        solution1 = arr[left]
        solution2 = arr[right]
        solution_val = value
    if abs(arr[left]) < abs(arr[right]):
        right -= 1
    else:
        left += 1

print(solution1, solution2)
