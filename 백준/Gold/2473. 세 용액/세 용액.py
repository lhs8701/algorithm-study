import sys


def twoPointer(numbers, left, pivot):
    right = len(numbers) - 1
    ans = [int(1e10), int(1e10), int(1e10)]
    while left < right:
        if numbers[left] == pivot:
            left += 1
            continue
        if numbers[right] == pivot:
            right -= 1
            continue

        if abs(numbers[left] + numbers[right] + pivot) < abs(sum(ans)):
            ans[0], ans[1], ans[2] = pivot, numbers[left], numbers[right]

        if numbers[left] + numbers[right] + pivot < 0:
            left += 1
        else:
            right -= 1
    return ans


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()

finalAns = [1e10, 1e10, 1e10]
for i in range(N - 1):
    pivot = numbers[i]
    num1, num2, num3 = twoPointer(numbers, i + 1, pivot)
    if abs(num1 + num2 + num3) < abs(sum(finalAns)):
        finalAns[0], finalAns[1], finalAns[2] = num1, num2, num3

finalAns.sort()
print(finalAns[0], finalAns[1], finalAns[2])
