def solution(slice, n):
    answer = n // slice + 1
    if n % slice == 0:
        answer -= 1
    return answer