def print_arr(list):
    for i in range(len(list)):
        print(list[i])
    print()


def func(arr, sub_len):
    full_len = len(arr)
    rotated_sub_list = []
    for i in range(0, full_len, sub_len):
        for j in range(0, full_len, sub_len):
            sub = [row[j:j + sub_len] for row in arr[i:i + sub_len]]
            rotated = list(zip(*sub[::-1]))
            rotated_sub_list.append(rotated)

    print(rotated_sub_list)
    print(len(rotated_sub_list))
    for i in range((full_len // sub_len) ** 2):
        row = i // sub_len
        col = i % sub_len
        for j in range(0, sub_len):
            for k in range(sub_len):
                arr[row * sub_len + j][col * sub_len + k] = rotated_sub_list[i][j][k]


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
print_arr(arr)

func(arr, 2)
print_arr(arr)
