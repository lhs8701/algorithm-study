import sys

alpha = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
sum = 0
input = sys.stdin.readline().rstrip()
for chr in input:
    sum += alpha[ord(chr) - ord('A')]
print(sum)
