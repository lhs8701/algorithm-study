import sys

N = int(sys.stdin.readline().rstrip())
words = []
for i in range(N):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))

words.sort()
words.sort(key=len)
for i in words:
    print(i)
