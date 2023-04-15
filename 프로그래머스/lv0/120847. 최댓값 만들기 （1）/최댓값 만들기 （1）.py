def solution(numbers):
    numbers.sort()
    length = len(numbers)
    return numbers[length-1] * numbers[length-2] 
    
