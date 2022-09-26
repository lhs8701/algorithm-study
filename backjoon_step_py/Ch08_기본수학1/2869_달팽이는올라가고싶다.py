import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())
ans = (V - A) // (A - B)
if (V - A) % (A - B) != 0:
    ans += 1
print(ans + 1)
