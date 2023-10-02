def main():
    n, c = map(int, input().split())
    numbers = list(map(int, input().split()))
    count = {}
    for idx, num in enumerate(numbers):
        if num in count:
            count[num][0] += 1
        else:
            count[num] = [1, idx, num]

    frequency = sorted(count.values(), key= lambda x: (-x[0], x[1]))
    result = []
    for fre in frequency:
        result += [fre[2]] * fre[0]
    print(*result)

if __name__ == "__main__":
    main()