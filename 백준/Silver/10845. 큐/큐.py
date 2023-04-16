import sys
N = int(sys.stdin.readline().rstrip())
queue = []
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command.__contains__('push'):
        temp, num = command.split()
        queue.append(int(num))
    elif command.__contains__('pop'):
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command.__contains__('size'):
        print(len(queue))
    elif command.__contains__('empty'):
        print(0 if queue else 1)
    elif command.__contains__('front'):
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
