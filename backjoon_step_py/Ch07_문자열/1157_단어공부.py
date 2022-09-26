import sys

alpha = [0] * 26
word = sys.stdin.readline().rstrip()
for i in range(len(word)):
    alpha[ord(word[i].lower()) - ord('a')] += 1

max = -1
flag = True
ans = 0
for i in range(26):
    if max < alpha[i]:
        flag = 0
        max = alpha[i]
        ans = i
    elif max == alpha[i]:
        flag = 1
if flag:
    print('?')
else:
    print(chr(ord('A') + ans))
