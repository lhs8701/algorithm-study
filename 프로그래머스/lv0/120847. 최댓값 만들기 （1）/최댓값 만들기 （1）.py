def solution(numbers):
    first  = max(numbers)
    first_idx = numbers.index(first)
    numbers.pop(first_idx)
    second = max(numbers)
    return first * second