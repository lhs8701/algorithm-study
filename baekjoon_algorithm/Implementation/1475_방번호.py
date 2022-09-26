import sys

arr = list(sys.stdin.readline().rstrip())
arr = list(map(int,arr))
numbers = [0]*10
cnt = 0
for i in range(len(arr)):
    if numbers[arr[i]] == 0:
        if arr[i] == 6:
            if numbers[9] != 0:
                numbers[9] -=1
                continue
        elif arr[i] == 9:
            if numbers[6] != 0:
                numbers[6] -= 1
                continue
        for j in range(10):
            numbers[j]+=1
        cnt+=1
    numbers[arr[i]] -= 1
print(cnt)
