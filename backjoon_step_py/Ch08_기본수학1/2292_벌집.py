import sys

N = int(sys.stdin.readline().rstrip())
cnt = 1
end = 1
while True:
    if N <= end:
        print(cnt)
        break
    end += cnt * 6
    cnt += 1
