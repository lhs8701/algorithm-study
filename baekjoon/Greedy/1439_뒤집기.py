import sys

S = list(sys.stdin.readline().rstrip())
S.append('x')
cnt = [0, 0]
for i in range(0, len(S) - 1):
    if S[i] != S[i + 1]:
        cnt[ord(S[i]) - ord('0')] += 1

print(min(cnt[0], cnt[1]))
