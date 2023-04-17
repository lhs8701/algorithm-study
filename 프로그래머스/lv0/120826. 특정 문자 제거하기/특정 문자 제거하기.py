def solution(my_string, letter):
    answer = []
    length = len(my_string)
    for i in range(length):
        if my_string[i] != letter:
            answer.append(my_string[i])
    return ''.join(answer)