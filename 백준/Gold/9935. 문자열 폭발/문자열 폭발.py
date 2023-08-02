import sys


class Stack:
    store = None
    top = None

    def __init__(self):
        self.store = []
        self.top = -1
        return

    def peek(self):
        return self.store[self.top]

    def push(self, elem):
        self.store.append(elem)
        self.top += 1
        return

    def pop(self):
        elem = self.store.pop()
        self.top -= 1
        return elem

    def popAll(self):
        temp = [i for i in self.store]
        temp.reverse()
        self.top = -1
        self.store.clear()
        return temp

    def isEmpty(self):
        return self.top == -1


string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
bombLength = len(bomb)
charOrder = {bomb[i]: i for i in range(bombLength)}
stack = Stack()
answer = []
for ch in string:
    if ch == bomb[0] or (not stack.isEmpty() and ch == bomb[charOrder[stack.peek()] + 1]):
        stack.push(ch)
    else:
        temp = stack.popAll()
        temp.reverse()
        for i in temp:
            answer.append(i)
        answer.append(ch)

    if not stack.isEmpty() and stack.peek() == bomb[-1]:
        for _ in range(bombLength):
            stack.pop()

if not stack.isEmpty():
    temp = stack.popAll()
    temp.reverse()
    for i in temp:
        answer.append(i)

if not answer:
    print("FRULA")
else:
    for i in answer:
        print(i, end='')
