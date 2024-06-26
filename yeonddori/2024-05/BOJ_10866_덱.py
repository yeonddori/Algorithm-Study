import sys

N = int(sys.stdin.readline())
deque = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deque.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(deque.pop(0) if deque else -1)
    elif command[0] == 'pop_back':
        print(deque.pop() if deque else -1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(0 if deque else 1)
    elif command[0] == 'front':
        print(deque[0] if deque else -1)
    elif command[0] == 'back':
        print(deque[-1] if deque else -1)
