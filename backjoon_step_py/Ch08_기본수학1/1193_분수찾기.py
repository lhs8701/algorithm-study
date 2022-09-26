import sys

X = int(sys.stdin.readline())
set = 1
end = 1
while X > end:
    set += 1
    end += set
if set % 2 == 1:
    print('{}/{}'.format(end - X + 1, set - (end - X)))
else:
    print('{}/{}'.format(set - (end - X), end - X + 1))
