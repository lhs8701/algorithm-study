def solution(num_list):
    size = len(num_list)
    even = len([i for i in num_list if i % 2 == 0])
    
    answer = [even, size - even]
    return answer