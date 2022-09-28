import sys

T = int(sys.stdin.readline().rstrip())
unit = [25, 10, 5, 1]
for i in range(T):
    C = int(sys.stdin.readline().rstrip())
    remain = C
    for j in unit:
        print(remain // j, end=" ")
        remain %= j
    print()
