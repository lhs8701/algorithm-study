def solution(array):
    print(1)

    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    sorted_dict = sorted(dict.items(), key = lambda item: -item[1])
    print(sorted_dict)
    if len(sorted_dict) > 1 and sorted_dict[0][1] == sorted_dict[1][1]:
        return -1
    else: 
        return sorted_dict[0][0]
