import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(N):
    alpha = [False] * 26
    word = sys.stdin.readline().rstrip()
    word += '?'
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            if alpha[ord(word[j]) - ord('a')]:
                cnt -= 1
                break
            alpha[ord(word[j]) - ord('a')] = True
    cnt += 1
print(cnt)
