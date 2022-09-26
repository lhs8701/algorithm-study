import sys

# selection sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(array):
    for i in range(len(array) - 1):
        minIdx = i
        for j in range(i, len(array)):
            if array[minIdx] > array[j]:
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i]


selection_sort(array)
print(array)

# insertion_sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


insertion_sort(array)
print(array)

# quick sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    pivot = start
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# quick sort (fast ver.)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]
    return quick_quick_sort(left_side) + [pivot] + quick_quick_sort(right_side)


array = quick_quick_sort(array)
print(array)

# counting sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


def counting_sort(array):
    count = [0] * 10
    sorted_array = [0] * len(array)
    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(array)):
        sorted_array[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
    return sorted_array


array = counting_sort(array)
print(array)
