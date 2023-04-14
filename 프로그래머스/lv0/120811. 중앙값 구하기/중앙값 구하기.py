def solution(array):
    array.sort()
    N = len(array)
    answer = array[N//2]
    return answer