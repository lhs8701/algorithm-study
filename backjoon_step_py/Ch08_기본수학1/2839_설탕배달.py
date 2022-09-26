import sys

N = int(sys.stdin.readline())
r = N
box_8 = 0
ans = sys.maxsize

while N >= box_8 * 8:
    if (N - box_8 * 8) % 3 == 0:
        if ans > box_8 * 2 + (N - box_8 * 8) // 3:
            ans = box_8 * 2 + (N - box_8 * 8) // 3
    if (N - box_8 * 8) % 5 == 0:
        if ans > box_8 * 2 + (N - box_8 * 8) // 5:
            ans = box_8 * 2 + (N - box_8 * 8) // 5
    box_8 += 1

print(-1 if ans == sys.maxsize else ans)
