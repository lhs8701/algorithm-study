import sys

str = sys.stdin.readline().rstrip()
pat = sys.stdin.readline().rstrip()

idx = 0
cnt = 0
l = len(str)
while idx < l:
    i = str[idx:l].find(pat)
    if i == -1:
        break
    cnt += 1
    idx += i + len(pat)

print(cnt)
