import sys


def find_prime():
    num = 2
    while num ** 2 <= N:
        i = num ** 2
        while i <= N:
            prime[i] = False
            i += num
        num += 1
        while num <= N and not prime[num]:
            num += 1


def next_right(idx):
    idx += 1
    if idx > N:
        return idx
    while idx <= N and not prime[idx]:
        idx += 1
    return idx


def next_left(idx):
    idx += 1
    while not prime[idx]:
        idx += 1
    return idx


N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(N + 1)]
prime = [True for _ in range(N + 1)]
find_prime()
prime[0] = False
prime[1] = False
left = 2
right = 2
cnt = 0

prev = 0
for i in range(1, N + 1):
    if prime[i]:
        dp[i] = prev + i
        prev = dp[i]

while left <= right and right <= N:
    if dp[right] - dp[left] + left == N:
        cnt += 1
        right = next_right(right)
    elif dp[right] - dp[left] + left < N:
        right = next_right(right)
    else:
        left = next_left(left)
print(cnt)
