def solution(array, height):
    array.sort(key=lambda x:-x)
    for i in range(len(array)):
        if array[i] <= height: 
            return i
    return len(array)