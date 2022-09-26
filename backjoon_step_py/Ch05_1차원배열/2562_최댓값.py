import sys

max_val = -1
idx = 0
for i in range(9):
    num = int(sys.stdin.readline().rstrip())
    if max_val < num:
        idx = i
        max_val = num
print(max_val)
print(idx + 1)
