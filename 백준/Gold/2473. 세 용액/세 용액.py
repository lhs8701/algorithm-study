import sys


def twoPointer(numbers, pivot):
    left, right = 0, len(numbers) - 1
    target = -pivot
    ans = [int(1e10), int(1e10)]
    while left < right:
        if numbers[left] == pivot:
            left += 1
            continue
        if numbers[right] == pivot:
            right -= 1
            continue

        val = numbers[left] + numbers[right]
        if abs(target - val) < abs(target - (ans[0] + ans[1])):
            ans[0], ans[1] = numbers[left], numbers[right]

        if val > target:
            right -= 1
        else:
            left += 1
    return ans[0], ans[1]

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()


ans = [1e10, 1e10, 1e10]
for pivot in numbers:
    num1, num2 = twoPointer(numbers, pivot)
    if abs(num1 + num2 + pivot) < abs(sum(ans)):
        ans[0], ans[1], ans[2] = num1, num2, pivot

ans.sort()
print(ans[0], ans[1], ans[2])