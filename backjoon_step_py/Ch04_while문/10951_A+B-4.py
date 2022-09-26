import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A+B)
    except:
        break
