import sys

num = int(sys.stdin.readline().rstrip())
if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
    print("1")
else:
    print("0")
