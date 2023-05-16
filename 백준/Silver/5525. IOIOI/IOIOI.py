import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()
cnt = [0 for _ in range(M)]
cnt[0] = 0 if S[0] == 'O' else 1
for i in range(1, M):
    if S[i - 1] == 'O':
        if S[i] == 'O':
            cnt[i] = 0
        else:
            cnt[i] = cnt[i - 1] + 1
    else:
        if S[i] == 'O':
            cnt[i] = cnt[i - 1] - 1 if cnt[i - 1] == 2 * N + 1 else cnt[i - 1] + 1
        else:
            cnt[i] = 1

print(cnt.count(2 * N + 1))
