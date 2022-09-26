# import sys
#
# N = int(sys.stdin.readline().rstrip())
# inputLine = list(map(int, sys.stdin.readline().rstrip().split()))
# inputLine.sort()
#
# arrAbs = []
# i = 0
# j = len(inputLine) - 1
# while i <= j:
#     if abs(inputLine[i]) < abs(inputLine[j]):
#         arrAbs.append(inputLine[j])
#         j -= 1
#     else:
#         arrAbs.append(inputLine[i])
#         i += 1
#
# arrDifference = []
# positiveFlag = False
# negativeFlag = False
# for i in range(1, len(arrAbs)):
#     sumVal = abs(arrAbs[i] + arrAbs[i - 1])
#     if not positiveFlag and arrAbs[i] > 0 and arrAbs[i - 1] > 0:
#         arrDifference.append((arrAbs[i], arrAbs[i - 1], sumVal))
#         postivieFlag = True
#     elif not negativeFlag and arrAbs[i] < 0 and arrAbs[i - 1] < 0:
#         arrDifference.append((arrAbs[i], arrAbs[i - 1], sumVal))
#         negativeFlagFlag = True
#     else:
#         arrDifference.append((arrAbs[i], arrAbs[i - 1], sumVal))
#
# arrDifference.sort(key=lambda x: x[2])
# print(min(arrDifference[0][0:2]), max(arrDifference[0][0:2]))
#

import sys

N = int(sys.stdin.readline().rstrip())
inputLine = list(map(int, sys.stdin.readline().rstrip().split()))
inputLine.sort()

start = 0
end = len(inputLine) - 1
minVal = sys.maxsize
num1 = 0
num2 = 0
while start != end:
    sum = inputLine[start] + inputLine[end]
    if minVal > abs(sum):
        minVal = abs(sum)
        num1 = inputLine[start]
        num2 = inputLine[end]
    if sum < 0:
        start += 1
    else:
        end -= 1

print(num1, num2)
