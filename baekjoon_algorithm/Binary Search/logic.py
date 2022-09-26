def lower_bound(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid + 1
    return left


def upper_bound(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid + 1
    return left
