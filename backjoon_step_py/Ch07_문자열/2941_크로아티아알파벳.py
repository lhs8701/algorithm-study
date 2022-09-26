import sys

line = sys.stdin.readline().rstrip()
cnt = 0
for i in range(len(line)):
    cnt += 1
    if line[i] == '=' or line[i] == '-':
        cnt -= 1
        if i > 1 and line[i] == '=' and line[i - 1] == 'z' and line[i - 2] == 'd':
            cnt -= 1
    elif line[i] == 'j':
        if i > 0 and (line[i - 1] == 'l' or line[i - 1] == 'n'):
            cnt -= 1
print(cnt)
