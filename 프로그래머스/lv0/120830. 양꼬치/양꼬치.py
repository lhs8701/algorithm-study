def solution(n, k):
    answer = 12000 * n + max(k - n // 10, 0) * 2000
    return answer