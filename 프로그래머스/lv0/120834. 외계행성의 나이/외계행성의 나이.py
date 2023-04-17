def solution(age):
    arr = list(map(int, str(age)))
    print(arr)
    answer = []
    for i in arr:
        answer.append(chr(97 + i))
    return "".join(answer)